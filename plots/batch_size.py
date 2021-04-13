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

log1 = np.loadtxt('../experiments/log_chpc_1.dat')
n_evals1 = log1[:,0] / 1e6
max_fitness1 = log1[:,3]
ax.plot(n_evals1, max_fitness1, label='239 Batch Size')

log2 = np.loadtxt('../experiments/log_chpc_3.dat')
n_evals2 = log2[:,0] / 1e6
max_fitness2 = log2[:,3]
ax.plot(n_evals2, max_fitness2, label='2390 Batch Size')

ax.set_title('Maximum Gait Performance Progress')
ax.legend()

plt.ylabel('Maximum gait performance ($m/s$)')
plt.xlabel('Evaluations ($millions$)')
# plt.ylim((0,0.5))

fig.tight_layout()

# plt.savefig('map_fitness.pdf')

plt.show()
