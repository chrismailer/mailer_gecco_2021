import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


def plot_footfall(sequences, dt=1/240):
	
	fig, ax = plt.subplots()
	fig.set_size_inches(w=4.7747, h=3.0)

	num = sequences.shape[1]
	duration = num*dt

	timestamp = np.linspace(0, duration, num)

	for i, sequence in enumerate(sequences):
		sequence = sequence * 1/240
		data = np.column_stack((timestamp, sequence))
		data = list(map(tuple, data))

		ax.broken_barh(data, (3*i, 2), facecolors='black')


	# ax.set_ylim(5, 35)
	ax.set_xlim(0, duration)
	ax.set_title('Footfall Sequence Diagram')
	ax.set_xlabel('Time ($s$)')
	ax.set_yticks([1, 4, 7, 10, 13, 16])
	ax.set_yticklabels(['Leg 1', 'Leg 2', 'Leg 3', 'Leg 4', 'Leg 5', 'Leg 6'])
	ax.grid(False)
	ax.invert_yaxis()
	ax.tick_params('y', length=0)
	# plt.legend(['Support'])

	fig.tight_layout()

	# plt.savefig('../Final Report/figures/tripod_sim_footfall.pdf')

	plt.show()


if __name__ == "__main__":
	sequences = np.random.choice([True, False], size=(6, 1200))
	plot(sequences)
