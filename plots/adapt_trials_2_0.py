import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('../experiments/adapt_trials_2_0.dat')
data = list(data)


fig, ax = plt.subplots()
ax.yaxis.grid(True)
ax.set_title('Adaptation number of trials')
bplot = ax.boxplot(data, notch=False, showfliers=True, labels=['1 & 2', '2 & 3', '3 & 4', '4 & 5', '5 & 6', '6 & 1'], widths=0.3, showmeans=True, patch_artist=True)

plt.ylabel('Number of trials')
plt.xlabel('Failed legs')

colors = ['tab:blue'] * 6

for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

def trials2time(x):
    return x * 5

def time2trials(x):
    return x / 5

secax = ax.secondary_yaxis('right', functions=(trials2time, time2trials))
secax.set_ylabel('Adaptation time (s)')

plt.ylim(0, 36)

plt.show()
