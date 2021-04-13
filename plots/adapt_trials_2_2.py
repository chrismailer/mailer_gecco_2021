import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

data = np.loadtxt('../experiments/adapt_trials_2_2.dat')
data = list(data)


fig, ax = plt.subplots()
fig.set_size_inches(w=4.7747, h=3.5)

ax.yaxis.grid(True)
ax.set_title('Adaptation number of trials')
ax.boxplot(data, notch=False, showfliers=True, widths=0.3, showmeans=True, patch_artist=True, labels=['1 \& 4', '2 \& 5', '3 \& 6'])

plt.ylabel('Number of trials')
plt.xlabel('Failed legs')

def trials2time(x):
    return x * 5

def time2trials(x):
    return x / 5

secax = ax.secondary_yaxis('right', functions=(trials2time, time2trials))
secax.set_ylabel('Adaptation time ($s$)')

plt.ylim(0, 12)

fig.tight_layout()

plt.show()
