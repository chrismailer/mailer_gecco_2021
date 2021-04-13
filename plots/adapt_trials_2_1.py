import numpy as np
import matplotlib.pyplot as plt

# get adaptation trial data
data = np.loadtxt('../experiments/adapt_trials_2_1.dat')
data = list(data)


fig, ax = plt.subplots()
ax.yaxis.grid(True)
ax.set_title('Adaptation number of trials')
ax.boxplot(data, notch=False, showfliers=True, widths=0.3, showmeans=True, patch_artist=True, labels=['1 & 3', '2 & 4', '3 & 5', '4 & 6', '5 & 1', '6 & 2'])

plt.ylabel('Number of trials')
plt.xlabel('Failed legs')

def trials2time(x):
    return x * 5

def time2trials(x):
    return x / 5

secax = ax.secondary_yaxis('right', functions=(trials2time, time2trials))
secax.set_ylabel('Adaptation time (s)')

plt.ylim(0, 24)

plt.show()
