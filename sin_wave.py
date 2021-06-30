import numpy as np
import matplotlib.pyplot as plt

def sin_wave(time, frequency, phase):

    return np.sin(2 * np.pi * frequency * time + phase)

time = np.linspace(0, 50, num = 250)
data = sin_wave(time, .133, .271)

sin_fig = plt.figure(figsize=(10.0, 6.0))
sin_plot = sin_fig.add_subplot(1, 1, 1)
sin_plot = plt.plot(time, data)
plt.title('sin wave')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()