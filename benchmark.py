from evaluate_gait import evaluate
import timeit

# radius, offset, stride, step, phase, duty_cycle
params = [	0.7, 0.3,
			0.6, 0.5, 0.2, 0.0, 0.5, 0.0, # leg 0
			0.6, 0.5, 0.2, 0.5, 0.5, 0.0, # leg 1
			0.6, 0.5, 0.2, 0.0, 0.5, 0.0, # leg 2
			0.6, 0.5, 0.2, 0.5, 0.5, 0.0, # leg 3
			0.6, 0.5, 0.2, 0.0, 0.5, 0.0, # leg 4
			0.6, 0.5, 0.2, 0.5, 0.5, 0.0] # leg 5

num = 10
runtime = timeit.timeit('evaluate(params)', setup='from __main__ import evaluate, params', number=num)
print(runtime / num, 's')
