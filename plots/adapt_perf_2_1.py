import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('../experiments/adapt_perf_2_1.dat')
data = list(data / 5)


fig, ax = plt.subplots()
ax.set_title('Walking performance after adaptation')
ax.boxplot(data, notch=False, showfliers=True, widths=0.3, showmeans=True, patch_artist=True, labels=['1 & 3', '2 & 4', '3 & 5', '4 & 6', '5 & 1', '6 & 2'])

plt.ylabel('Walking performance (m/s)')
plt.xlabel('Failed leg')

plt.ylim(0, 0.5)

plt.show()
