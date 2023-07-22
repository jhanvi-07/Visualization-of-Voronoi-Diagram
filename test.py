import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from datetime import datetime

points = np.loadtxt('./input.txt')
# Compute Voronoi diagram
vor = Voronoi(points) 
# Visualize Voronoi diagram
fig, ax = plt.subplots(figsize=(16, 9))
voronoi_plot_2d(vor, ax=ax)

# Plot input points
ax.plot(points[:, 0], points[:, 1], 'r.', markersize=10)

# Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# Display plot
plt.show()

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
fig.savefig('out/voronoi_' + dt_string + '.png')
