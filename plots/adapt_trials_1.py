import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('../experiments/adapt_trials_1.dat')
data = list(data)

fig, ax = plt.subplots()
ax.yaxis.grid(True)
ax.set_title('Adaptation number of trials')
bplot = ax.boxplot(data, notch=False, showfliers=True, labels=['leg 1', 'leg 2', 'leg 3', 'leg 4', 'leg 5', 'leg 6'], widths=0.3, showmeans=True, patch_artist=True)

plt.ylabel('Number of trials')
plt.xlabel('Failed leg')


def trials2time(x):
    return x * 5

def time2trials(x):
    return x / 5

secax = ax.secondary_yaxis('right', functions=(trials2time, time2trials))
secax.set_ylabel('Adaptation time (s)')

plt.ylim(0, 10) # 50s

plt.show()
