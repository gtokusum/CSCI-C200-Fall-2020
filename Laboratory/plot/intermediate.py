# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(2, 1, 1) # two rows, one column, first plot

# fig2 = plt.figure()
# ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])


# import numpy as np
# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2*np.pi*t)
# line, = ax.plot(t, s, color='blue', lw=2)
# plt.show()
# del ax.lines[0]
# ax.lines.remove(line)  # one or the other, not both!
# xtext = ax.set_xlabel('my xdata') # returns a Text instance
# ytext = ax.set_ylabel('my ydata')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# fig.subplots_adjust(top=0.8)
# ax1 = fig.add_subplot(211)
# ax1.set_ylabel('volts')
# ax1.set_title('a sine wave')

# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2*np.pi*t)
# line, = ax1.plot(t, s, color='blue', lw=2)

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
# n, bins, patches = ax2.hist(np.random.randn(1000), 50,
#                             facecolor='yellow', edgecolor='yellow')
# ax2.set_xlabel('time (s)')

# plt.show()


# import matplotlib.ticker as ticker

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# fig, ax = plt.subplots()
# ax.plot(100*np.random.rand(20))

# formatter = ticker.FormatStrFormatter('$%1.2f')
# ax.yaxis.set_major_formatter(formatter)

# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_visible(False)
#     tick.label2.set_visible(True)
#     tick.label2.set_color('green')

# plt.show()

# import matplotlib.patches as mpatches
# import matplotlib.pyplot as plt

# red_patch = mpatches.Patch(color='red', label='The red data')
# plt.legend(handles=[red_patch])

# plt.show()

# import matplotlib.lines as mlines

# blue_line = mlines.Line2D([], [], color='blue', marker='*',
#                           markersize=15, label='Blue stars')
# plt.legend(handles=[blue_line])

# plt.show()


# plt.subplot(211)
# plt.plot([1, 2, 3], label="test1")
# plt.plot([3, 2, 1], label="test2")

# # Place a legend above this subplot, expanding itself to
# # fully use the given bounding box.
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
#            ncol=2, mode="expand", borderaxespad=0.)

# plt.subplot(223)
# plt.plot([1, 2, 3], label="test1")
# plt.plot([3, 2, 1], label="test2")
# # Place a legend to the right of this smaller subplot.
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# plt.show()


# line1, = plt.plot([1, 2, 3], label="Line 1", linestyle='--')
# line2, = plt.plot([3, 2, 1], label="Line 2", linewidth=4)

# # Create a legend for the first line.
# first_legend = plt.legend(handles=[line1], loc='upper right')

# # Add the legend manually to the current Axes.
# ax = plt.gca().add_artist(first_legend)

# # Create another legend for the second line.
# plt.legend(handles=[line2], loc='lower right')

# plt.show()


# from matplotlib.legend_handler import HandlerLine2D

# line1, = plt.plot([3, 2, 1], marker='o', label='Line 1')
# line2, = plt.plot([1, 2, 3], marker='o', label='Line 2')

# plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
# plt.show()

# from numpy.random import randn

# z = randn(10)

# red_dot, = plt.plot(z, "ro", markersize=15)
# # Put a white cross over some of the data.
# white_cross, = plt.plot(z[:5], "w+", markeredgewidth=3, markersize=15)

# plt.legend([red_dot, (red_dot, white_cross)], ["Attr A", "Attr A+B"])

# plt.show()


# from matplotlib.legend_handler import HandlerLine2D, HandlerTuple

# p1, = plt.plot([1, 2.5, 3], 'r-d')
# p2, = plt.plot([3, 2, 1], 'k-o')

# l = plt.legend([(p1, p2)], ['Two keys'], numpoints=1,
#                handler_map={tuple: HandlerTuple(ndivide=None)})
# plt.show()

