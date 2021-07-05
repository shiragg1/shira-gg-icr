#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def sin_wave(time, frequency, phase):

    return np.sin(2 * np.pi * frequency * time + phase)

time = np.linspace(0, 50, num = 250)
data = sin_wave(time, .133, .271)

sin_fig = plt.figure(figsize=(10.0, 18.0))
sin_plot = sin_fig.add_subplot(3, 1, 1)
sin_plot = plt.plot(time, data)
plt.title('sin wave')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

data_noisy = data + np.random.uniform(0, 0.5, data.shape)
sin_plot_noisy = sin_fig.add_subplot(3, 1, 2)
sin_plot_noisy = plt.plot(time, data_noisy)
plt.title('sin wave with random noise added')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

sp = np.fft.fft(data_noisy)
freq = np.fft.fftfreq(time.shape[-1])
spectra_plot = sin_fig.add_subplot(3, 1, 3)
spectra_plot = plt.plot(freq, sp.real, freq, sp.imag)
plt.title('spectra of the noisy sine wave')

plt.show()