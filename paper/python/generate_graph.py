import matplotlib.pyplot as plt

# For both graphs
max_weights = [100, 200, 300, 400, 500]
# For the max weight vs time graph
#
dynamic_timings = [n / 1000 for n in [7446320, 14733273, 24533937, 29605866, 38435691]]
increasing_weight_timings = [n / 1000 for n in [31775, 35600, 50913, 41883, 46523]]
decreasing_value_timings = [n / 1000 for n in [22007, 25499, 32682, 32846, 36866]]
decreasing_ratio_timings = [n / 1000 for n in [30532, 33547, 41684, 33837, 42071]]

# For the second graph of max weight vs accuracy 
dynamic_accuracy = [100.0, 100.0, 100.0, 100.0, 100.0]
increasing_weight_accuracy = [84.3615, 85.9055, 87.1212, 89.4167, 95.5788]
decreasing_value_accuracy = [73.1946, 88.6910, 95.0205, 98.4185, 99.8065]
decreasing_ratio_accuracy = [99.8515, 99.8826, 99.9342, 99.9409, 99.9844]

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

line_dynamic_timings = ax.plot(max_weights, dynamic_timings, 'b', label="Dynamic Algorithm", linewidth=2)
line_increasing_weight = ax.plot(max_weights, increasing_weight_timings, 'g', label="Increasing Weight", linewidth=2)
line_decreasing_value = ax.plot(max_weights, decreasing_value_timings, 'r', label="Decreasing Value", linewidth=2)
line_decreasing_ratio = ax.plot(max_weights, decreasing_ratio_timings, 'c',label="Decreasing Ratio", linewidth=2)


# plot the same line again so i can use it in the key for ax2
line_increasing_weight = ax2.plot(max_weights, increasing_weight_timings, 'g', label="Increasing Weight", linewidth=2)
line_decreasing_value = ax2.plot(max_weights, decreasing_value_timings, 'r', label="Decreasing Value", linewidth=2)
line_decreasing_ratio = ax2.plot(max_weights, decreasing_ratio_timings, 'c', label="Decreasing Ratio", linewidth=2)

ax.legend(handles=[line_dynamic_timings[0], line_increasing_weight[0], line_decreasing_value[0], line_decreasing_ratio[0]])

# Add dashes on side of graph
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal


ax.set_ylim(7000, 60000) # outliers
ax2.set_ylim(20, 60) # most of the data
# hide the axis between the two
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')
ax2.xaxis.tick_bottom()


# axis(xmin, xmax, ymin, ymax)
#plt.axis([100, 500, 0, 500000])
plt.ylabel('Average Time Taken in Microseconds') 
plt.xlabel('Maximum Weight')
ax.set_title('Time to Calculate Items to take with Maximum Available Weight (N)') 
#plt.show()
plt.savefig('timeGraph.png')
