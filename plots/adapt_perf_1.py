import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt


# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


data = np.loadtxt('../experiments/adapt_perf_1.dat')
data = list(data / 5)

t_statistic, p_value = stats.ttest_ind(data[0], data[1], equal_var=False)
print(t_statistic)

fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=3.5)
ax.yaxis.grid(True)
ax.set_title('Performance after adaptation')
ax.boxplot(data, notch=False, showfliers=True, labels=['leg 1', 'leg 2', 'leg 3', 'leg 4', 'leg 5', 'leg 6'], widths=0.3, showmeans=True, patch_artist=True)

plt.ylabel('Adapted performance (m/s)')
plt.xlabel('Failed leg')

plt.ylim(0, 0.5)

fig.tight_layout()

# plt.savefig('histogram.pgf')

plt.show()
