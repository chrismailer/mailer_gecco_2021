import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=3.5)

axins = ax.inset_axes([0.4, 0.2, 0.2, 0.4])

for num in range(1,11):
	log = np.loadtxt('../maps/log_%d.dat' % num)
	n_evals = log[:,0] / 1e6
	mean_fitness = log[:,3]/5
	ax.plot(n_evals, mean_fitness, label='Map %d' % num)
	axins.plot(n_evals, mean_fitness)


ax.set_title('Mean Fitness Progress')
ax.legend()

plt.ylabel('Mean fitness ($m/s$)')
plt.xlabel('Evaluations ($millions$)')

# inset axes
x1, x2, y1, y2 = 0, 0.4, 0, 0.015
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
ax.indicate_inset_zoom(axins)

fig.tight_layout()

# plt.savefig('histogram.pgf')

plt.show()
