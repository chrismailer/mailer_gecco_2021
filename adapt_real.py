from MBOA import MBOA
from plots.map import plot_map
import numpy as np
import time

sim = 1.4456
real = 1.3125

counter = 0
data = np.loadtxt('./real_experiments/experiment_3.dat')

def evaluate(x):
	global counter
	global data
	fitness = data[counter, 1]
	descriptor = np.zeros((6,0))
	counter += 1
	return fitness, descriptor


if __name__ == "__main__":
		
	num_its = []
	best_indexes = []
	best_perfs = []

	# need to redefine the evaluate function each time to include the failed leg
	num_it, best_index, best_perf, new_map = MBOA("./maps/map_2.dat", "centroids_40000_6.dat", evaluate, max_iter=40)
	np.savetxt('./real_experiments/adapted_map_3.dat', new_map)
	num_its.append(num_it)
	best_indexes.append(best_index)
	best_perfs.append(best_perf)

	# print('Failed Leg: %d' % failed_leg_1)
	print(num_it, best_index, best_perf)
