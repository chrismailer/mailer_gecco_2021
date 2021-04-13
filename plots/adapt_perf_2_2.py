import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


data = np.loadtxt('../experiments/adapt_perf_2_2.dat')
data = list(data / 5)

t_statistic, p_value = stats.ttest_ind(data[0], data[1], equal_var=False)
print(p_value)

fig, ax = plt.subplots()
ax.set_title('Walking performance after adaptation')
ax.boxplot(data, notch=False, showfliers=True, widths=0.3, showmeans=True, patch_artist=True, labels=['1 & 4', '2 & 5', '3 & 6'])

plt.ylabel('Walking performance (m/s)')
plt.xlabel('Failed leg')

plt.ylim(0, 0.5)

plt.show()
