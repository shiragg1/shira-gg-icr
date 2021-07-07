import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
 
# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
#plotting sphere
u = np.linspace(0, np.pi, 50)
v = np.linspace(0, 2 * np.pi, 50)
 
a = np.outer(np.sin(u), np.sin(v))
b = np.outer(np.sin(u), np.cos(v))
c = np.outer(0.5*np.cos(u), 0.5*np.ones_like(v)) + 0.05

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
 
ax.plot_surface(a, b, c, zorder=1)

#plotting gaussian
x=np.linspace(-5,5, num=100)
y=np.linspace(-5,5, num=100)
x, y = np.meshgrid(x, y)
 
z = -np.exp(-0.2*x**2-0.2*y**2)/4

ax.plot_surface(x,y,z, cmap="winter", zorder=0, alpha=0.6)
ax.set_axis_off()
 
plt.show()
