import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc

# Some global settings for plotting
fontsize = 12
textsize = 10
linewidth = 1.5
labelsize = 10

# default figure size, golden ratio!
figsize = (5.2, 5.2/1.618)
figdpi = 500

gridwidth = 0.3

matplotlib.rcParams['font.family'] = ['Times New Roman']
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['mathtext.default'] = 'rm'

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

#==========================================================================

# First define the figure and get the axes object
fig, ax = plt.subplots( figsize=figsize, dpi=figdpi)

# Ticks
ax.tick_params( direction='in', axis='both', which='both', labelsize=labelsize)
ax.tick_params( direction='out', axis='y', which='both', labelsize=labelsize)

# Grids
ax.grid( which='both', axis='both', linestyle='--', linewidth=gridwidth, color='lightgrey')

# X-Y labels
ax.set_xlabel( r'Nucleon energy [MeV]', fontsize=fontsize, loc='right')
ax.set_xscale('log')
ax.set_xlim( [10,10000] )

ax.set_yscale('log')
ax.set_ylabel( r'Nucleon flux [MeV$^{-1}$cm$^{-2}$s$^{-1}$]', fontsize=fontsize, loc='top')
#ax.set_ylim( [5e-11,5e-3] )

# Plot it on the y axis
lines = ax.plot( )

labs = [l.get_label() for l in lines]
ax.legend( lines, labs, loc='lower left', fontsize=fontsize-2, handlelength=1.5, framealpha=0.7, frameon=False )

#alternatively, just do
# plt.legend( ... )

#===================================================================================================

# The case of dual axis

ax2 = ax.twinx()

ax2.set_ylabel(r'Cross section [mb/MeV]', fontsize=fontsize, loc='top')
ax2.set_yscale('log')
#ax2.set_ylim([1e-6,5e+2])
#ax.set_ylabel(r'log$_{10}$(S2$_{\rm c}$ [phd])',fontsize=12,loc='top')

lines = ax2.plot( energy, xe_xsec[x], label=xe_labs[x], linewidth=linewidth/2, linestyle='--')

# labels
labs = [l.get_label() for l in lines]
ax2.legend( lines, labs, loc='center right', fontsize=fontsize-2, handlelength=1.5, framealpha=0.7, frameon=False, ncol=1)
