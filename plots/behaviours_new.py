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

mean_fitness = np.empty((16737,10))
max_fitness = np.empty((16737,10))
n_evals = []

for n in range(1,11):
	log = np.loadtxt('../maps/log_%d.dat' % n)
	n_evals = log[:,0] / 1e6
	max_fitness[:,n-1] = log[:,1]
	# np.append(max_fitness, max_fit, axis=1)

ax.plot(n_evals, np.mean(max_fitness, axis=1), label='Maximum')
ax.fill_between(n_evals, np.min(max_fitness, axis=1), np.max(max_fitness, axis=1), alpha=0.3)

ax.set_title('Number of Gaits Progression')
# ax.legend()

plt.ylabel('Number of unique gaits')
plt.xlabel('Evaluations ($million$)')
plt.ylim((0,44000))
plt.xlim((0,40))
plt.grid(True, which='major', axis='y')
plt.yticks([0, 10000, 20000, 30000, 40000])

fig.tight_layout()

# plt.savefig('../../Final Report/figures/map_gaits_progression.pdf')

plt.show()
