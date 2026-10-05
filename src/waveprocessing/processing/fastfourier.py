import h5py
import numpy as np
import matplotlib.pyplot as plt

from waveprocessing.data.reading import load_strain #import a helper function to get strain data
from waveprocessing.processing.preprocessing import clean_strain

FILE = "data/raw/GW150914_H1.hdf5"


def main():
    strain, sampling_rate = load_strain(FILE) #Get Strain Data
    strain = clean_strain(strain)

    fast_fourier_transform = np.fft.rfft(strain) #Calculate FFT with numpy
    frequencies = np.fft.rfftfreq(len(strain), 1 / sampling_rate) #Creating The frequency values

    amplitude = np.abs(fast_fourier_transform) #Magnitude of complex numbers

    #Plotting the data with matplotlib
    plt.figure(figsize= (10,5))
    plt.plot(frequencies, amplitude) #Plot frequency on x and amplitude on y axis
    plt.xlabel("Frequency - Hz")
    plt.ylabel("FFT Magnitude")
    plt.title("GW150914 - LIGO H1 Frequency vs Amplitude")
    plt.grid(True)
    plt.xlim(20, 500)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

    