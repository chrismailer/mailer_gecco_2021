import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=4.0)


log1 = np.loadtxt('../experiments/log_init_1%.dat')
n_evals1 = log1[:,0] / 1e6
max_fitness1 = log1[:,3] / 5
ax.plot(n_evals1, max_fitness1, label='1\% Initialisation')

log10 = np.loadtxt('../experiments/log_init_10%.dat')
n_evals10 = log10[:,0] / 1e6
max_fitness10 = log10[:,3] / 5
ax.plot(n_evals10, max_fitness10, label='10\% Initialisation')


ax.set_title('Average Gait Performance Progress')
ax.legend()

plt.ylabel('Average gait performance ($m/s$)')
plt.xlabel('Evaluations ($millions$)')
plt.ylim((0,0.3))
plt.xlim((0,40))

fig.tight_layout()

plt.savefig('../../Final Report/figures/infill_mean_fitness.pdf')

# plt.show()
