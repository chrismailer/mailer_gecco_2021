import numpy as np
import matplotlib
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# load data
data = np.loadtxt("../real_experiments/failure_1&4_4.dat")
fitness = data[:,1]

fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=3.5)

ax.yaxis.grid(True)
ax.set_title('')
ax.plot(fitness)

plt.ylabel('')
plt.xlabel('')

# plt.ylim(0, 0.5)

fig.tight_layout()

# plt.savefig('histogram.pgf')

plt.show()