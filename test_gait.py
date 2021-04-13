from hexapod.controllers.kinematic import Controller, reshape
from hexapod.simulator import Simulator
from plots.footfall import plot_footfall
import numpy as np

# np.set_printoptions(precision=4)
# np.warnings.filterwarnings('error', category=np.VisibleDeprecationWarning)


# function responsible for testing the gait parameters and returning the descriptor and performance
# pass in a 32 length array of parmeters between 0.0 and 1.0
def test_gait(leg_params, body_height=0.14, velocity=0.3, duration=5.0, visualiser=True, collisions=False, failed_legs=[]):
	# controller will return an error if parameters are not feasible
	controller = Controller(leg_params, body_height=body_height, velocity=velocity, crab_angle=-np.pi/6)
	# initialise simulator
	simulator = Simulator(controller, follow=True, visualiser=visualiser, collision_fatal=collisions, failed_legs=failed_legs)
	# initialise reward and descriptor
	contact_sequence = np.full((6, 0), False)
	# simulator returns error if collision occurs
	for t in np.arange(0, duration, step=simulator.dt):
		try:
			simulator.step()
		except RuntimeError as error:
			print(error)
			reward = 0
			break
		contact_sequence = np.append(contact_sequence, simulator.supporting_legs().reshape(-1,1), axis=1)
	reward = simulator.base_pos()[0]
	# summarise descriptor
	descriptor = np.sum(contact_sequence, axis=1) / np.size(contact_sequence, axis=1)
	# plot footfall diagram
	plot_footfall(contact_sequence)

	simulator.terminate()

	return reward, descriptor


# place to test out gaits

if __name__ == "__main__":
	from hexapod.controllers.kinematic import tripod_gait, quadruped_gait, wave_gait

	gait_map = np.loadtxt('./maps/5k/map_1.dat')
	row_index = np.argmax(gait_map, axis=0)[0]
	# gait_map = gait_map[gait_map[:,0] > 2.0]
	# row_index = np.random.randint(0, gait_map.shape[0])
	# row_index = 19079

	fitness = gait_map[row_index, 0]
	desc = gait_map[row_index, 1:7]
	centroid = gait_map[row_index, 7:13]
	params = gait_map[row_index, 13:]
	body_height, velocity, leg_params = reshape(params)

	print(fitness)

	# print(params)

	fitness, descriptor = test_gait(leg_params, body_height=body_height, velocity=velocity, duration=5.0, collisions=False, visualiser=True, failed_legs=[])
	print('fitness:', fitness, 'm')
	print('descriptor:', descriptor)
	# plot(descriptor)
