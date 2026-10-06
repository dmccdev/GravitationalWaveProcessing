import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

from waveprocessing.data.reading import load_strain
from waveprocessing.processing.preprocessing import clean_strain
from waveprocessing.processing.whitening import whiten

FILE = "data/raw/GW150914_H1.hdf5"

#Lowcut and Highcut are quite unique to the example currently
def bandpassfilter(strain, sampling_rate, lowcut = 20.0, highcut = 500.0, order = 4):
    nyquist = 0.5 * sampling_rate #Calculate nyquist frequency

    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low,high], btype = "band")
    filtered_strain = filtfilt(b, a, strain)
    return filtered_strain

def main():

    strain, sampling_rate = load_strain(FILE)
    strain = clean_strain(strain)
    strain_whitened, strain_fft_whitened, frequencies_fft = whiten(strain, sampling_rate)

    strain_filtered = bandpassfilter(strain_whitened, sampling_rate)
    time = np.arange(0, len(strain)) / sampling_rate

    plt.figure(figsize = (12,5))
    plt.plot(time, strain_filtered, color = "darkorange", alpha = 0.9, label = "Filtered and Whitened Strain")
    plt.xlim(16.24, 16.45)
    plt.xlabel("Time - seconds")
    plt.ylabel("Filtered Strain Amplitude")
    plt.title("GW150914 - Whitened and Filtered LIGO strain vs time")
    plt.grid(True, ls = "--", alpha = 0.5)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()



