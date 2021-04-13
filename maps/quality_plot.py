import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter
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

global_performance = np.loadtxt('global_performance.csv', delimiter=',')
global_reliability = np.loadtxt('global_reliability.csv', delimiter=',')
precision = np.loadtxt('precision.csv', delimiter=',')
coverage = np.loadtxt('coverage.csv', delimiter=',') / 1000

# customisation
box_widths = 0.4
plot_width = 1.6
plot_height = 2.0
color_20 = 'tab:orange'
color_40 = 'tab:blue'
flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='darkgray')

labels = ['20k', '40k']

t_statistic, p_value = stats.ttest_ind(global_performance[:,0], global_performance[:,1])
print(p_value)
t_statistic, p_value = stats.ttest_ind(global_reliability[:,0], global_reliability[:,1])
print(p_value)
t_statistic, p_value = stats.ttest_ind(precision[:,0], precision[:,1])
print(p_value)
t_statistic, p_value = stats.ttest_ind(coverage[:,0], coverage[:,1])
print(p_value)


# global performance
fig, ax = plt.subplots()
fig.set_size_inches(w=plot_width, h=plot_height)
ax.yaxis.grid(True)
ax.set_title('Performance')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

bp20 = ax.boxplot(global_performance[:,0], positions=[1], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)
bp40 = ax.boxplot(global_performance[:,1], positions=[2], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)

set_box_color(bp20, color_20)
set_box_color(bp40, color_40)

start, end = ax.get_ylim()
start = 0.73
ax.set_ylim((start, end))

plt.xticks([1, 2], labels)
plt.tight_layout(pad=0.1)
plt.savefig("../figures/global_performance_plot.pdf")
plt.show()


# global reliability
fig, ax = plt.subplots()
fig.set_size_inches(w=plot_width, h=plot_height)
ax.yaxis.grid(True)
ax.set_ylim((start, end))
# ax.yaxis.set_ticks(np.arange(start, end, 0.01))
ax.set_title('Reliability')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

bp20 = ax.boxplot(global_reliability[:,0], positions=[1], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)
bp40 = ax.boxplot(global_reliability[:,1], positions=[2], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)

set_box_color(bp20, color_20)
set_box_color(bp40, color_40)

plt.xticks([1, 2], labels)
plt.tight_layout(pad=0.1)
plt.savefig("../figures/reliability_plot.pdf")
plt.show()


# precision
fig, ax = plt.subplots()
fig.set_size_inches(w=plot_width, h=plot_height)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.yaxis.grid(True)
ax.set_ylim((start, end))
# ax.yaxis.set_ticks(np.arange(start, end, 0.01))
ax.set_title('Precision')

bp20 = ax.boxplot(precision[:,0], positions=[1], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)
bp40 = ax.boxplot(precision[:,1], positions=[2], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)

set_box_color(bp20, color_20)
set_box_color(bp40, color_40)

plt.xticks([1, 2], labels)
plt.tight_layout(pad=0.1)
plt.savefig("../figures/precision_plot.pdf")
plt.show()


# coverage
fig, ax = plt.subplots()
fig.set_size_inches(w=plot_width, h=plot_height)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.yaxis.grid(True)
# ax.set_ylim((0.85, 0.95))
# start, end = ax.get_ylim()
ax.set_ylim((start, end))
# ax.yaxis.set_ticks(np.arange(start, end, 0.01))
ax.set_title('Coverage')

flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='darkgray')
bp20 = ax.boxplot(coverage[:,0], positions=[1], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)
bp40 = ax.boxplot(coverage[:,1], positions=[2], widths=box_widths, showfliers=True, flierprops=flierprops, patch_artist=True)

set_box_color(bp20, color_20)
set_box_color(bp40, color_40)

plt.xticks([1, 2], labels)
plt.tight_layout(pad=0.1)
plt.savefig("../figures/coverage_plot.pdf")
plt.show()
