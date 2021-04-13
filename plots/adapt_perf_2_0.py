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

data = np.loadtxt('../experiments/adapt_perf_2_0.dat')
data = list(data / 5)


fig, ax = plt.subplots()
fig.set_size_inches(w=6, h=3.5)
ax.yaxis.grid(True)
ax.set_title('Walking performance after adaptation')
ax.boxplot(data, notch=False, showfliers=True, widths=0.3, showmeans=True, patch_artist=True, labels=['1 \& 2', '2 \& 3', '3 \& 4', '4 \& 5', '5 \& 6', '6 \& 1'])

plt.ylabel('Walking performance ($m/s$)')
plt.xlabel('Failed leg')

plt.ylim(0, 0.5)

# plt.savefig('histogram.pgf')

plt.show()
