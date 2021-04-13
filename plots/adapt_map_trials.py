import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt

# number of trials per map across all failure scenarios

np.set_printoptions(precision=3)

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# load data
scenario1 = np.loadtxt('../experiments/adapt_trials_1.dat')
scenario2 = np.loadtxt('../experiments/adapt_trials_2_0.dat')
scenario3 = np.loadtxt('../experiments/adapt_trials_2_1.dat')
scenario4 = np.loadtxt('../experiments/adapt_trials_2_2.dat')

data = np.vstack((scenario1, scenario2, scenario3, scenario4))

p_values = []
for map_i in range(10):
	for map_j in range(10):
		if map_j == map_i: continue
		t_statistic, p_value = stats.ttest_ind(data[:,map_i], data[:,map_j])
		p_values.append(p_value)
print(np.min(p_values))


fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=2.5)
ax.axhline(24, color='r', linestyle='--')
ax.yaxis.grid(True)
ax.set_title('Number of Adaptation Trials')
bplot = ax.boxplot(data, notch=False, showfliers=True, labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], widths=0.3, showmeans=True, patch_artist=True)

plt.ylabel('Number of trials')
plt.xlabel('Behaviour-performance map')

def trials2time(x):
    return x * 5

def time2trials(x):
    return x / 5

secax = ax.secondary_yaxis('right', functions=(trials2time, time2trials))
secax.set_ylabel('Adaptation duration ($s$)')

# color map red
# patch = bplot['boxes'][5]
# patch.set_facecolor('red')

plt.ylim(0, 40)

fig.tight_layout()

plt.savefig('../../Final Report/figures/adapt_trials_maps.pdf')

# plt.show()
