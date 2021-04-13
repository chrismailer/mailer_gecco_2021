from hexapod.controllers.kinematic import Controller, reshape
from hexapod.simulator import Simulator
from adapt.MBOA import MBOA
import numpy as np

# parameters
map_count = 10
niches = 10 #k
failure_scenario = 0

S0 = [[]]
S1 = [[1],[2],[3],[4],[5],[6]]
S2 = [[1,4],[2,5],[3,6]]
S3 = [[1,3],[2,4],[3,5],[4,6],[5,1],[6,2]]
S4 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]]

scenarios = [S0, S1, S2, S3, S4]
failures = scenarios[failure_scenario]

num_its = np.zeros((len(failures), map_count))
best_indexes = np.zeros((len(failures), map_count))
best_perfs = np.zeros((len(failures), map_count))

for failure_index, failed_legs in enumerate(failures):
	print("Failed legs:", failed_legs)
	for map_num in range(1, map_count+1):
		print("Testing map:", map_num)

		# need to redefine the evaluate function each time to include the failed leg
		def evaluate_gait(x, duration=5.0):
			body_height, velocity, leg_params = reshape(x)
			try:
				controller = Controller(leg_params, body_height=body_height, velocity=velocity, crab_angle=-np.pi/6)
			except:
				return 0
			simulator = Simulator(controller, visualiser=False, collision_fatal=False, failed_legs=failed_legs)
			fitness, contacts = 0, np.full((6, 0), False)
			for t in np.arange(0, duration, step=simulator.dt):
				try:
					simulator.step()
				except RuntimeError as error:
					fitness = 0
					break
				fitness = simulator.base_pos()[0]
				contacts = np.append(contacts, simulator.supporting_legs().reshape(-1,1), axis=1)
			# summarise descriptor
			descriptor = np.sum(contacts, axis=1) / np.size(contacts, axis=1)
			descriptor = np.nan_to_num(descriptor, nan=0.0, posinf=0.0, neginf=0.0)
			simulator.terminate()
			return fitness

		num_it, best_index, best_perf, new_map = MBOA(f"./maps/{niches}k_half/map_{map_num}.dat", f"./centroids/centroids_{niches}000_6.dat", evaluate_gait, max_iter=40, print_output=False)

		num_its[failure_index, map_num-1] = num_it
		best_indexes[failure_index, map_num-1] = best_index
		best_perfs[failure_index, map_num-1] = best_perf


# np.savetxt(f"./experiments/sim/{niches}k_half/trials_{failure_scenario}.dat", num_its, '%d')
# np.savetxt(f"./experiments/sim/{niches}k_half/perfs_{failure_scenario}.dat", best_perfs)

np.savetxt(f"./experiments/sim/{niches}000_niches/trials_{failure_scenario}.dat", num_its, '%d')
np.savetxt(f"./experiments/sim/{niches}000_niches/perfs_{failure_scenario}.dat", best_perfs)
