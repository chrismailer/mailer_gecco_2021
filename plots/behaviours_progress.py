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

axins = ax.inset_axes([0.3, 0.3, 0.2, 0.4])

for num in range(1,11):
	log = np.loadtxt('../maps/log_%d.dat' % num)
	n_evals = log[:,0] / 1e6
	coverage = (log[:,1] / 40000) * 100
	ax.plot(n_evals, coverage, label='Map %d' % num)
	axins.plot(n_evals, coverage)


ax.set_title('Number of Different Gaits')
ax.legend()

# inset axes
x1, x2, y1, y2 = 0, 0.4, 0, 2
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
ax.indicate_inset_zoom(axins)

plt.ylabel('Number of gaits')
plt.xlabel('Evaluations ($million$)')
plt.ylim(0, 42000)
plt.xlim(0, 40)

fig.tight_layout()

# plt.savefig('histogram.pgf')

plt.show()
