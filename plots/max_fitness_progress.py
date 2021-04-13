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
fig.set_size_inches(w=4.7747, h=4.0)


for num in range(1,11):
	log = np.loadtxt('../maps/log_%d.dat' % num)
	n_evals = log[:,0] / 1e6
	max_fitness = log[:,2] / 5
	ax.plot(n_evals, max_fitness, label='Map %d' % num)


ax.set_title('Maximum Fitness Progress')
ax.legend()

plt.ylabel('Maximum fitness ($m/s$)')
plt.xlabel('Evaluations ($millions$)')
plt.ylim((0,0.5))
plt.grid(True, which='major', axis='y')

fig.tight_layout()

# plt.savefig('map_fitness.pdf')

plt.show()
