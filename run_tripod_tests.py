from hexapod.controllers.kinematic import Controller, reshape, tripod_gait
from hexapod.simulator import Simulator
import numpy as np

# runs through all of the failure scenarios and tests the performance of the tripod gait

def simulate_gait(leg_params, body_velocity, body_height, failed_legs, duration=5.0):
	try:
		controller = Controller(leg_params, body_height=body_height, velocity=body_velocity, crab_angle=-np.pi/6)
	except:
		return 0
	simulator = Simulator(controller, visualiser=False, collision_fatal=False, failed_legs=failed_legs)
	# simulator.set_foot_friction(1.0)
	fitness = 0
	for t in np.arange(0, duration, step=simulator.dt):
		simulator.step()
	fitness = simulator.base_pos()[0]
	simulator.terminate()
	return fitness


S0 = [[]]
S1 = [[1],[2],[3],[4],[5],[6]]
S2 = [[1,4],[2,5],[3,6]]
S3 = [[1,3],[2,4],[3,5],[4,6],[5,1],[6,2]]
S4 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]]

duration = 5.0
scenarios = [S0, S1, S2, S3, S4]

for failure_scenario, failures in enumerate(scenarios):
	performances = []
	for failed_legs in failures:
		fitness = simulate_gait(tripod_gait, 0.3, 0.14, failed_legs=failed_legs, duration=duration)
		performances.append(max(fitness / duration, 0.0))
	np.savetxt(f"./experiments/sim/tripod_{failure_scenario}.dat", performances)
