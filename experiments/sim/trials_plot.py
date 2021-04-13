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

for scenario in range(1,5):
    sim_data_20.append(list(np.loadtxt(f'./20000_niches/trials_{scenario}.dat').flatten()))
    sim_data_40.append(list(np.loadtxt(f'./40000_niches/trials_{scenario}.dat').flatten()))

# adaptation stats
print('adaptation statistics')

# map size stats
print('map size statistics')
t_statistic, p_value = stats.ttest_ind(sim_data_20[0], sim_data_40[0])
print('S1:', p_value)
t_statistic, p_value = stats.ttest_ind(sim_data_20[1], sim_data_40[1])
print('S2:', p_value)
t_statistic, p_value = stats.ttest_ind(sim_data_20[2], sim_data_40[2])
print('S3:', p_value)
t_statistic, p_value = stats.ttest_ind(sim_data_20[3], sim_data_40[3])
print('S4:', p_value)


ticks = ['S1', 'S2', 'S3', 'S4']
color_20 = 'tab:orange'
color_40 = 'tab:blue'
box_width = 0.4

fig, ax = plt.subplots()
fig.set_size_inches(w=3.3, h=2.0)
ax.yaxis.grid(True)
ax.set_title('Number of Adaptation Trials')
ax.set_xlabel('Failure scenario')
ax.set_ylabel('Trials')

flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='darkgray')
positions = np.array(range(len(sim_data_40)))*2.0
bp20 = plt.boxplot(sim_data_20, positions=positions-0.25, widths=box_width, showfliers=True, flierprops=flierprops, patch_artist=True)
bp40 = plt.boxplot(sim_data_40, positions=positions+0.25, widths=box_width, showfliers=True, flierprops=flierprops, patch_artist=True)
set_box_color(bp20, color_20)
set_box_color(bp40, color_40)

# ax.axhline(120/5, color='tab:gray', linestyle='-.', label='2 minute line')

custom_lines = [mpatches.Patch(color=color_20), mpatches.Patch(color=color_40)]
plt.legend(custom_lines, ['20k', '40k'])

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 45)
plt.tight_layout(pad=0.1)

plt.savefig("../../figures/trials_plot.pdf")
plt.show()