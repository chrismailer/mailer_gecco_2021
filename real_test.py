#!/usr/bin/python
import sys
import numpy as np
from MBOA import MBOA
from hexpy.controllers.kinematic import reshape

# need np.flip as leg order was defined by Ross as CW not CCW

# function to evaluate adaptation on the real hexapod robot
# gait parameters are printed to the console formatted in C++ and can be copied directly into the Hexapod code
# input the fitness into the console once the evaluation has ended
def real_eval(x):
	body_height, velocity, leg_params = reshape(x)
	
	print("\ndouble footVelocity = {:f};".format(velocity*1000))
	print("double bodyHeight = {:f};".format(body_height*1000))
	radius = np.flip(leg_params[:,0]*1000)
	print("double radialDistances[6] =", "{", "{:f}, {:f}, {:f}, {:f}, {:f}, {:f}".format(*radius), "};")
	offset = np.flip(leg_params[:,1])
	print("double angleOffsets[6] =", "{", "{:f}, {:f}, {:f}, {:f}, {:f}, {:f}".format(*offset), "};")
	step = np.flip(leg_params[:,2]*1000)
	print("double stepHeights[6] =", "{", "{:f}, {:f}, {:f}, {:f}, {:f}, {:f}".format(*step), "};")
	phase = np.flip(leg_params[:,3])
	print("double phaseOffsets[6] =", "{", "{:f}, {:f}, {:f}, {:f}, {:f}, {:f}".format(*phase), "};")
	duty_factor = np.flip(leg_params[:,4])
	print("double dutyFactors[6] =", "{", "{:f}, {:f}, {:f}, {:f}, {:f}, {:f}".format(*duty_factor), "};\n")

	fitness = float(input("Fitness (m): "))
	return fitness, None


if __name__ == "__main__":

	n_map = int(sys.argv[1]) # map number argument

	map_filename = "./maps/map_%d.dat" % n_map

	print("Starting map number:", n_map)
	
	num_it, best_index, best_perf = MBOA(map_filename, "./centroids_40000_6.dat", real_eval, max_iter=40)

	print("Done map number:", n_map)
	print("No. iterations:", num_it)
	print("Best performance:", best_perf)
	print("Best index:", best_index)
