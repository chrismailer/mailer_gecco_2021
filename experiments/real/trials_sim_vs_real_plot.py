import matplotlib.patches as mpatches
import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    'pgf.texsystem': "pdflatex",
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color='black')

# load simulated results
S0 = np.loadtxt('../sim/40000_niches/trials_0.dat').flatten()
S1 = np.loadtxt('../sim/40000_niches/trials_1.dat').flatten()
S2 = np.loadtxt('../sim/40000_niches/trials_2.dat').flatten()
sim = np.array((S0, S1, S2))

# load control results
# control1 = np.loadtxt('control_experiment.dat') / 5
# control2 = np.loadtxt('../experiments/tripod_failure_1.dat').flatten()
# control3 = np.loadtxt('../experiments/tripod_failure_2_2.dat').flatten()
# control = list([control2, control3])

# load real experiment data
real1 = np.loadtxt('experiment_1.dat').shape[0]
real2 = np.loadtxt('experiment_2.dat').shape[0]
real3 = np.loadtxt('experiment_3.dat').shape[0]
real4 = np.loadtxt('experiment_4.dat').shape[0]
real5 = np.loadtxt('experiment_5.dat').shape[0]
real6 = np.loadtxt('experiment_6.dat').shape[0]
real = np.array(([1,real1], [1,real2], [2,real3], [2,real4], [3,real5], [3,real6]))

t_statistic, p_value = stats.ttest_ind(real.flatten(), np.hstack(sim))
print(p_value)

normal_tripod_mean = np.mean(np.loadtxt('../sim/tripod_0.dat')) / 5

# plotting graph
fig, ax = plt.subplots()
fig.set_size_inches(w=3.3, h=2.0)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.set_title('Number of Adaptation Trials')

# ax.axhline(120/5, color='tab:red', linestyle='--', label='2 minute threshold')

# ax.axhline(failed_tripod_mean, color='tab:red', linestyle='--', label='Failed Tripod Gait')
# ax.axhspan(failed_tripod_max, failed_tripod_min, color='tab:red', alpha=0.25)
flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='darkgray')
bp = ax.boxplot(sim, showfliers=True, flierprops=flierprops, labels=['None', 'S1', 'S2'], widths=0.2, patch_artist=True)
real_scatter = ax.scatter(real[:,0], real[:,1], marker='x', color='tab:green')

for i, point in enumerate(real):
	if i in [0,3,4]:
		plt.text(point[0]+0.05, point[1], str(i+1), verticalalignment='bottom')
	else:
		plt.text(point[0]+0.05, point[1], str(i+1), verticalalignment='top')

set_box_color(bp, 'tab:blue')

plt.ylabel('Trials')
plt.xlabel('Failure scenario')
# plt.xticks(np.arange(3), ['None', 'Scenario 1', 'Scenario 2'])
plt.ylim(0, 40)
sim_patch = mpatches.Patch(color='tab:blue')
plt.legend((real_scatter, sim_patch), ('Reality', 'Simulated'), loc='upper left')

fig.tight_layout(pad=0.1)

plt.savefig("../../figures/sim_vs_real_trials_plot.pdf")
plt.show()
