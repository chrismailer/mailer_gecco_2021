import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    'pgf.texsystem': "pdflatex",
    'pdf.fonttype': 42,
	'ps.fonttype': 42,
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

n_maps = 20

mean_fit_40 = np.zeros((16737,n_maps))
max_fit_40 = np.zeros((16737,n_maps))

mean_fit_20 = np.zeros((16737,n_maps))
max_fit_20 = np.zeros((16737,n_maps))

niches_20 = np.zeros((16737,n_maps))
niches_40 = np.zeros((16737,n_maps))

n_evals = []

for n in range(1, n_maps+1):
	log_20 = np.loadtxt(f'./20k/log_{n}.dat')
	log_40 = np.loadtxt(f'./40k/log_{n}.dat')
	max_fit_20[:,n-1] = log_20[:,2] / 5.0
	max_fit_40[:,n-1] = log_40[:,2] / 5.0
	mean_fit_20[:,n-1] = log_20[:,3] / 5.0
	mean_fit_40[:,n-1] = log_40[:,3] / 5.0
	n_evals = log_20[:,0] / 1e6
	# np.append(max_fitness, max_fit, axis=1)
	niches_20[:, n-1] = log_20[:,1] / 200
	if n > 10:
		niches_40[:, n-1] = log_40[:,1] / 400
	else:
		niches_40[:, n-1] = log_40[:,1] / 400 - 13.7 # accounts for error where failed gaits were mistakenly put into a niche

max_fit_20[max_fit_20 <= 0] = np.nan
max_fit_40[max_fit_40 <= 0] = np.nan

# customisation
color_20k = 'tab:orange'
color_40k = 'tab:blue'
fill_alpha = 0.3
custom_lines = [Line2D([0], [0], color=color_20k, lw=4), Line2D([0], [0], color=color_40k, lw=4)]
labels = ['20k', '40k']
height = 2.5

# max fitness plot
fig, ax = plt.subplots()
fig.set_size_inches(w=2.2, h=height)

ax.grid(True, which='major', axis='y')
ax.set_xlabel('Evaluations ($\\times10^6$)')
ax.set_ylabel('Gait speed ($m/s$)')
ax.set_xlim((0,40))
ax.set_ylim((0,0.6))
ax.axhline(0.5, color='gray', linestyle='-.', label='maximum')
ax.text(0.7, 0.51, 'maximal', horizontalalignment='left', verticalalignment='bottom')

n_evals = log_20[:,0] / 1e6
ax.plot(n_evals, np.nanmean(max_fit_20, axis=1), label='20000', color=color_20k)
ax.fill_between(n_evals, np.min(max_fit_20, axis=1), np.max(max_fit_20, axis=1), alpha=fill_alpha, facecolor=color_20k)

n_evals = log_40[:,0] / 1e6
ax.plot(n_evals, np.nanmean(max_fit_40, axis=1), label='40000', color=color_40k)
ax.fill_between(n_evals, np.min(max_fit_40, axis=1), np.max(max_fit_40, axis=1), alpha=fill_alpha, facecolor=color_40k)

plt.legend(custom_lines, labels, loc='lower right')

fig.tight_layout(pad=0.1)
plt.savefig("../figures/maps_max.pdf")
plt.show()


# mean fitness plot
fig, ax = plt.subplots()
fig.set_size_inches(w=2.2, h=height)

ax.grid(True, which='major', axis='y')
ax.set_xlabel('Evaluations ($\\times10^6$)')
ax.set_ylabel('Gait speed ($m/s$)')
ax.set_xlim((0,40))
ax.set_ylim((0,0.6))
ax.axhline(0.5, color='gray', linestyle='-.', label='maximum')
ax.text(0.7, 0.51, 'maximal', horizontalalignment='left', verticalalignment='bottom')

n_evals = log_20[:,0] / 1e6
ax.plot(n_evals, np.nanmean(mean_fit_20, axis=1), label='20000', color=color_20k)
ax.fill_between(n_evals, np.min(mean_fit_20, axis=1), np.max(mean_fit_20, axis=1), alpha=fill_alpha, facecolor=color_20k)

n_evals = log_40[:,0] / 1e6
ax.plot(n_evals, np.nanmean(mean_fit_40, axis=1), label='40000', color=color_40k)
ax.fill_between(n_evals, np.min(mean_fit_40, axis=1), np.max(mean_fit_40, axis=1), alpha=fill_alpha, facecolor=color_40k)

plt.legend(custom_lines, labels, loc='lower right')

fig.tight_layout(pad=0.1)
plt.savefig("../figures/maps_avg.pdf")
plt.show()


# map coverage plot
fig, ax = plt.subplots()
fig.set_size_inches(w=2.2, h=height)

ax.grid(True, which='major', axis='y')
ax.set_xlabel('Evaluations ($\\times10^6$)')
ax.set_ylabel('Coverage ($\%$)')
ax.set_xlim((0,40))
ax.set_ylim((0,100))

ax.set_title('Coverage')
n_evals = log_20[:,0] / 1e6
ax.plot(n_evals, np.nanmean(niches_20, axis=1), label='20000', color=color_20k)
ax.fill_between(n_evals, np.min(niches_20, axis=1), np.max(niches_20, axis=1), alpha=fill_alpha, facecolor=color_20k)

n_evals = log_40[:,0] / 1e6
ax.plot(n_evals, np.nanmean(niches_40, axis=1), label='40000', color=color_40k)
ax.fill_between(n_evals, np.min(niches_40, axis=1), np.max(niches_40, axis=1), alpha=fill_alpha, facecolor=color_40k)

plt.legend(custom_lines, labels, loc='lower right')

fig.tight_layout(pad=0.1)
plt.savefig("../figures/maps_coverage.pdf")
plt.show()
