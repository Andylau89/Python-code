import numpy as np
from matplotlib import pyplot as plt
############111111111111111111111111111111111111111111111111111111

# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Long live the king")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()

from mpl_toolkits import mplot3d
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline);

plt.show()
