import numpy as np
import matplotlib.pyplot as plt
 
#plotting gaussian
x=np.linspace(-5,5, num=100)
y=np.linspace(-5,5, num=100)
x, y = np.meshgrid(x, y)
 
z = -np.exp(-0.2*x**2-0.2*y**2)/4
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, cmap="winter")
ax.set_axis_off()
 
 
#plotting sphere
u = np.linspace(0, np.pi, 50)
v = np.linspace(0, 2 * np.pi, 50)
 
a = np.outer(np.sin(u), np.sin(v))
b = np.outer(np.sin(u), np.cos(v))
c = np.outer(0.4*np.cos(u), 0.4*np.ones_like(v)) + 0.7
 
ax.plot_surface(a, b, c)
 
plt.show()
