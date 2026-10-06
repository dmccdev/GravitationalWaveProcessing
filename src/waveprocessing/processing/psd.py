from scipy.signal import welch
import matplotlib.pyplot as plt


def calculate_psd(strain, sampling_rate) -> tuple:


    frequencies, psd = welch(x = strain, fs = sampling_rate, nperseg = 4096)

    return frequencies, psd


def main():
    from waveprocessing.data.reading import load_strain
    FILE = "data/raw/GW150914_H1.hdf5"

    strain, sampling_rate = load_strain(FILE)

    # Calculate PSD
    frequencies, psd = calculate_psd(strain,sampling_rate)

    # Plot PSD
    plt.figure(figsize=(10, 5))

    plt.loglog(frequencies, psd)

    plt.xlabel("Frequency - Hz")
    plt.ylabel("Power Spectral Density")
    plt.title("GW150914 - LIGO H1 Power Spectral Density")

    plt.grid(True)

    # Only show frequencies we're interested in
    plt.xlim(20, 2000)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()