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

# load data
scenario1 = np.loadtxt('../experiments/adapt_trials_1.dat').flatten()
scenario2 = np.loadtxt('../experiments/adapt_trials_2_2.dat').flatten()
scenario3 = np.loadtxt('../experiments/adapt_trials_2_1.dat').flatten()
scenario4 = np.loadtxt('../experiments/adapt_trials_2_0.dat').flatten()

# load real experiment data
# real1 = np.loadtxt('../real_experiments/failure_1_2.dat')
# real2 = np.loadtxt('../real_experiments/orient/failure_1_2.dat')
# real3 = np.loadtxt('../real_experiments/failure_1&4_4.dat')
# real4 = np.loadtxt('../real_experiments/orient/failure_1&4_6.dat')

# real5 = np.loadtxt('../real_experiments/failure_0_2.dat')
# real6 = np.loadtxt('../real_experiments/orient/failure_0_1.dat')

t_statistic, p_value = stats.ttest_1samp(scenario4, 24)
print(p_value)

sim = list([scenario1, scenario2, scenario3, scenario4])

print(sim)

fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=3.5)
ax.yaxis.grid(True)
ax.set_title('Number of Adaptation Trials')
ax.axhline(24, color='r', linestyle='--')

bplot = ax.boxplot(sim, notch=True, showfliers=True, labels=['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4'], widths=0.2, showmeans=True, patch_artist=True)

# ax.plot(1, len(real1), marker='*', color='r')
# ax.plot(1, len(real2), marker='*', color='r')
# ax.plot(4, len(real3), marker='*', color='r')
# ax.plot(4, len(real4), marker='*', color='r')

# ax.plot(0, len(real5), marker='*', color='r')
# ax.plot(0, len(real6), marker='*', color='r')

plt.ylabel('Number of trials')
plt.xlabel('Failure')


def trials2time(x):
    return x * 5

def time2trials(x):
    return x / 5

secax = ax.secondary_yaxis('right', functions=(trials2time, time2trials))
secax.set_ylabel('Adaptation duration ($s$)')

plt.ylim(0, 40)
plt.text(0.7, 24+0.5, '2 minutes', horizontalalignment='left')

fig.tight_layout()

# plt.savefig('../../Final Report/figures/adapt_trials_sim.pdf')

# plt.show()
