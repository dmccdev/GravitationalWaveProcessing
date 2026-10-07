import numpy as np
import matplotlib.pyplot as plt


sampling_rate = 4096

time = np.arange(0, 1, 1 / sampling_rate)

frequency = np.linspace(30, 250, len(time))

phase = 2 * np.pi * np.cumsum(frequency) / sampling_rate

template = np.sin(phase)

plt.figure(figsize=(12, 5))

plt.plot(time, template)

plt.xlabel("Time - seconds")
plt.ylabel("Amplitude")
plt.title("Simple Gravitational-Wave Chirp Template")

plt.grid(True)

plt.tight_layout()
plt.show()
