import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy import stats

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

# load data
sim_data_20 = []
sim_data_40 = []
tripod_data = []
tripod_mean_data = []

for scenario in range(5):
    data_20 = list(np.loadtxt(f'./20000_niches/perfs_{scenario}.dat').flatten() / 5)
    data_40 = list(np.loadtxt(f'./40000_niches/perfs_{scenario}.dat').flatten() / 5)
    tripod = list(np.loadtxt(f'tripod_{scenario}.dat').flatten())
    sim_data_20.append(data_20)
    sim_data_40.append(data_40)
    tripod_data.append(tripod)
    tripod_mean_data.append(np.mean(tripod))

tripod_mean = np.mean(np.loadtxt('tripod_0.dat'))

# performance stats
print("performance stats")
for scenario in range(1,5):
    t_statistic, p_value = stats.ttest_ind(sim_data_20[scenario] + sim_data_40[scenario], tripod_data[scenario])
    print(f'S{scenario}:', p_value)

# map size stats
print('map size statistics')
for scenario in range(4):
    t_statistic, p_value = stats.ttest_ind(sim_data_20[scenario], sim_data_40[scenario])
    print(f'S{scenario+1}:', p_value)


ticks = ['None', 'S1', 'S2', 'S3', 'S4']
box_width = 0.4
color_20 = 'tab:orange'
color_40 = 'tab:blue'

fig, ax = plt.subplots()
fig.set_size_inches(w=3.3, h=2.0)
ax.set_axisbelow(True)
ax.yaxis.grid(True)
ax.set_title('Adapted Walking Speed')
ax.set_xlabel('Failure scenario')
ax.set_ylabel('Speed ($m/s$)')

flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='darkgray')
meanline = dict(linestyle='-', color='black')
meanpoint = dict(marker='D', markeredgecolor='black', markerfacecolor='red')
positions = np.array(range(len(sim_data_40)))*2.0

bp20 = plt.boxplot(sim_data_20, positions=positions-0.25, widths=box_width, showfliers=True, flierprops=flierprops, patch_artist=True)
bp40 = plt.boxplot(sim_data_40, positions=positions+0.25, widths=box_width, showfliers=True, flierprops=flierprops, patch_artist=True)

# bp = plt.boxplot(tripod_data, positions=positions, widths=0.4, showfliers=True, flierprops=flierprops, notch=True, showmeans=True, patch_artist=True)

plt.scatter(positions, tripod_mean_data, marker='*', color='tab:red')

# ax.axhline(tripod_mean, color='tab:red', linestyle='-.', label='Default Tripod Gait')

set_box_color(bp20, color_20)
set_box_color(bp40, color_40)
# set_box_color(bp, 'tab:red')

custom_lines = [mpatches.Patch(color=color_20), mpatches.Patch(color=color_40)]
plt.legend(custom_lines, ['20k', '40k'])

plt.xticks(range(0, len(ticks)*2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 0.6)
plt.tight_layout(pad=0.1)

plt.savefig("../../figures/perfs_plot.pdf")
plt.show()
