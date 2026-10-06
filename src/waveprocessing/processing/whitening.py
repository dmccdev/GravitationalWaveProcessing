import numpy as np
import matplotlib.pyplot as plt
from waveprocessing.processing.fastfourier import calculate_fft
from waveprocessing.data.reading import load_strain #import a helper function to get strain data
from waveprocessing.processing.psd import calculate_psd
from waveprocessing.processing.preprocessing import clean_strain


FILE = "data/raw/GW150914_H1.hdf5"

def whiten(strain, sampling_rate) -> tuple:

    strain_fft, frequencies_fft = calculate_fft(strain, sampling_rate)
    frequencies_psd, strain_psd = calculate_psd(strain, sampling_rate)
    strain_psd_interpolated = np.interp(frequencies_fft, frequencies_psd, strain_psd)

    strain_fft_whitened = strain_fft / np.sqrt(strain_psd_interpolated) #Calculate Whitened Data

    strain_whitened = np.fft.irfft(a = strain_fft_whitened, n = len(strain)) #Reverse FFT

    return strain_whitened, strain_fft_whitened, frequencies_fft

def main():
    strain, sampling_rate = load_strain(FILE)
    strain = clean_strain(strain)

    strain_whitened, strain_fft_whitened, frequencies_fft = whiten(strain, sampling_rate)
    time = np.arange(0, len(strain)) / sampling_rate #Generates an array from 0 to length of strain array with stepsize of 1 multiplied by sample duration
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8))

    ax1.plot(frequencies_fft, np.abs(strain_fft_whitened), color = "teal", alpha = 0.7)
    ax1.set_xscale("log")
    ax1.set_xlim(20, 2000)
    ax1.set_xlabel("Frequency - Hz")
    ax1.set_ylabel("Whitened FFT Magnitude")
    ax1.set_title("Whitened Frequency Spectrum")
    ax1.grid(True, which = "both", ls = "--", alpha = 0.5)

    ax2.plot(time, strain_whitened, color = "navy", alpha = 0.6)
    ax2.set_xlim(time[0], time[-1])
    ax2.set_xlabel("Time - seconds")
    ax2.set_ylabel("Whitened Strain Amplitude")
    ax2.set_title("Whitened Time-Series Signal")
    ax2.grid(True, ls = "--", alpha = 0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()




