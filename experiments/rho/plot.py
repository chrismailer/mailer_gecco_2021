import numpy as np
import matplotlib.pyplot as plt

# Create some mock data

niches = 40000
perfs = np.loadtxt(f'perfs_{niches}.dat') / 5
trials = np.loadtxt(f'iters_{niches}.dat')

rhos = np.linspace(0.1, 0.9, num=perfs.shape[1])

fig, ax1 = plt.subplots()

ax1.set_xlabel("$\\rho$ parameter")
ax1.set_ylabel("Speed ($m/s$)")
ax1.set_ylim(0, 0.5)
ax1.plot(rhos, np.mean(perfs, axis=0), color='tab:blue')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel("Trials)")  # we already handled the x-label with ax1
ax2.set_ylim(0, 22)
ax2.plot(rhos, np.mean(trials, axis=0), color='tab:orange')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
