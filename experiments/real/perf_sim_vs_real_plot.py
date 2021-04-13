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

n_maps = 20

max_perf = []
for n in range(n_maps):
	log = np.loadtxt(f'../../maps/niches_40000/log_{n+1}.dat')
	max_perf.append(np.max(log[-1:,2]) / 5)

# load simulated results
S0 = np.loadtxt('../sim/40000_niches/perfs_0.dat').flatten() / 5.0
S1 = np.loadtxt('../sim/40000_niches/perfs_1.dat').flatten() / 5.0
S2 = np.loadtxt('../sim/40000_niches/perfs_2.dat').flatten() / 5.0
sim = list([S0, S1, S2])

# load control results
tripod_0 = np.mean(np.loadtxt('../sim/tripod_0.dat').flatten())
tripod_1 = np.mean(np.loadtxt('../sim/tripod_1.dat').flatten())
tripod_2 = np.mean(np.loadtxt('../sim/tripod_2.dat').flatten())
tripod = list([tripod_0, tripod_1, tripod_2])

# load real experiment data
real1 = np.max(np.loadtxt('experiment_1.dat')[:,1]).flatten() / 5
real2 = np.max(np.loadtxt('experiment_2.dat')[:,1]).flatten() / 5
real3 = np.max(np.loadtxt('experiment_3.dat')[:,1]).flatten() / 5
real4 = np.max(np.loadtxt('experiment_4.dat')[:,1]).flatten() / 5
real5 = np.max(np.loadtxt('experiment_5.dat')[:,1]).flatten() / 5
real6 = np.max(np.loadtxt('experiment_6.dat')[:,1]).flatten() / 5
real = np.array([[1,real1], [1,real2], [2,real3], [2,real4], [3,real5], [3,real6]])

t_statistic, p_value = stats.ttest_ind(real.flatten(), np.hstack(sim))
print(p_value)

normal_tripod_mean = np.mean(np.loadtxt('../sim/tripod_0.dat')) / 5

ticks = ['None', 'S1', 'S2']
sim_color = 'tab:blue'
box_width = 0.2

# plotting graph
fig, ax = plt.subplots()
fig.set_size_inches(w=3.3, h=2.0)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.set_title('Adapted Walking Speed')

# ax.axhline(failed_tripod_mean, color='tab:red', linestyle='--', label='Failed Tripod Gait')
# ax.axhspan(failed_tripod_max, failed_tripod_min, color='tab:red', alpha=0.25)
flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='darkgray')
bp = ax.boxplot(sim, showfliers=True, flierprops=flierprops, widths=box_width, patch_artist=True)
real_scatter = ax.scatter(real[:,0], real[:,1], marker='x', color='tab:green')
ref_scatter = ax.scatter([1,2,3], tripod, marker='*', color='tab:red')

for i, point in enumerate(real):
	if i in [1,2,5]:
		plt.text(point[0]+0.05, point[1], str(i+1), verticalalignment='bottom')
	else:
		plt.text(point[0]+0.05, point[1], str(i+1), verticalalignment='top')

set_box_color(bp, sim_color)

plt.ylabel('Speed ($m/s$)')
plt.xlabel('Failure scenario')
plt.ylim(0, 0.5)
plt.xticks(range(1,len(ticks)+1), ticks)
sim_patch = mpatches.Patch(color='tab:blue')
plt.legend((ref_scatter, real_scatter, sim_patch), ('Reference', 'Real', 'Simulated'), loc='lower left')

fig.tight_layout(pad=0.1)

plt.savefig("../../figures/sim_vs_real_perfs_plot.pdf")
plt.show()
