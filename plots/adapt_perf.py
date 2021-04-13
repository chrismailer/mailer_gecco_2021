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

# load simulated results
scenario1 = np.loadtxt('../experiments/sim/40000_niches/adapt_perf_1.dat').flatten() / 5
scenario2 = np.loadtxt('../experiments/sim/40000_niches/adapt_perf_2_2.dat').flatten() / 5
scenario3 = np.loadtxt('../experiments/sim/40000_niches/adapt_perf_2_1.dat').flatten() / 5
scenario4 = np.loadtxt('../experiments/sim/40000_niches/adapt_perf_2_0.dat').flatten() / 5

# load control results
control1 = np.loadtxt('../experiments/sim/tripod_1.dat').flatten()
control2 = np.loadtxt('../experiments/sim/tripod_2.dat').flatten()
control3 = np.loadtxt('../experiments/sim/tripod_3.dat').flatten()
control4 = np.loadtxt('../experiments/sim/tripod_4.dat').flatten()

# load real experiment data
# real1 = np.loadtxt('../real_experiments/failure_1_2.dat')
# real2 = np.loadtxt('../real_experiments/orient/failure_1_2.dat')
# real3 = np.loadtxt('../real_experiments/failure_1&4_4.dat')
# real4 = np.loadtxt('../real_experiments/orient/failure_1&4_6.dat')

# real5 = np.loadtxt('../real_experiments/failure_0_2.dat')
# real6 = np.loadtxt('../real_experiments/orient/failure_0_1.dat')

normal_tripod_mean = np.mean(np.loadtxt('../experiments/sim/tripod_no_failure.dat')) / 5

data = list([scenario1, scenario2, scenario3, scenario4])
control = list([control1, control2, control3, control4])
# failed_tripod_max, failed_tripod_mean, failed_tripod_min = np.max(control), np.mean(control), np.min(control)

# t_statistic, p_value = stats.ttest_1samp(scenario3, normal_tripod_mean)
t_statistic, p_value = stats.ttest_ind(scenario1, scenario2)
print(p_value)

# plotting graph
fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=3.5)
ax.yaxis.grid(True)
ax.set_title('Adapted Performance')

# ax.axhline(failed_tripod_mean, color='tab:red', linestyle='--', label='Failed Tripod Gait')
# ax.axhspan(failed_tripod_max, failed_tripod_min, color='tab:red', alpha=0.25)

ax.axhline(normal_tripod_mean, color='tab:red', linestyle='--', label='Default Tripod Gait')

bplot1 = ax.boxplot(data, notch=True, showfliers=True, labels=['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4'], widths=0.2, showmeans=True, patch_artist=True)
bplot2 = ax.boxplot(control, notch=True, showfliers=True, labels=['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4'], widths=0.2, showmeans=True, patch_artist=True)

# ax.plot(1, max(real1[:,1])/5, marker='*', color='r')
# ax.plot(1, max(real2[:,1])/5, marker='*', color='r')
# ax.plot(4, max(real3[:,1])/5, marker='*', color='r')
# ax.plot(4, max(real4[:,1])/5, marker='*', color='r')

# ax.plot(0, max(real5[:,1])/5, marker='*', color='r')
# ax.plot(0, max(real6[:,1])/5, marker='*', color='r')

plt.ylabel('Performance ($m/s$)')
plt.xlabel('Failure')
plt.ylim(0, 0.5)
for patch in bplot2['boxes']:
	patch.set_facecolor('tab:orange')

# plt.text(0.7, failed_tripod_mean+0.005, 'tripod gait with failure', horizontalalignment='left')
plt.text(0.7, normal_tripod_mean-0.006, 'tripod gait without failures', horizontalalignment='left', verticalalignment='top')
fig.tight_layout()
plt.legend([bplot1["boxes"][0], bplot2["boxes"][0]], ['Adaptation', 'Tripod'], loc='upper right')

# plt.savefig('../../Final Report/figures/adapted_perf_sim.pdf')
plt.show()
