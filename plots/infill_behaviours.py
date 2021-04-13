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
fig.set_size_inches(w=4.7747, h=3.5)

log1 = np.loadtxt('../experiments/log_init_1%.dat')
n_evals1 = log1[:,0] / 1e6
coverage1 = log1[:,1]
ax.plot(n_evals1, coverage1, label='1\% Initialisation')

log10 = np.loadtxt('../experiments/log_init_10%.dat')
n_evals10 = log10[:,0] / 1e6
coverage10 = log10[:,1]
ax.plot(n_evals10, coverage10, label='10\% Initialisation')

ax.set_title('Number of Different Gaits')
ax.legend()

plt.ylabel('Number of gaits')
plt.xlabel('Evaluations ($million$)')
plt.ylim(0, 42000)
plt.xlim(0, 40)

fig.tight_layout()

plt.savefig('../../Final Report/figures/infill_variation_behaviours.pdf')

# plt.show()
