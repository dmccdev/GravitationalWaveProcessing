from scipy.signal import welch
import matplotlib.pyplot as plt


def calculate_psd(strain, sampling_rate, nperseg=4096):
    """
    Calculate the Power Spectral Density (PSD) of a strain signal.

    Parameters
    ----------
    strain : array-like
        LIGO strain time-series data.
    sampling_rate : float
        Sampling frequency of the strain data in Hz.
    nperseg : int, optional
        Length of each segment used by Welch's method.

    Returns
    -------
    frequencies : numpy.ndarray
        Frequencies in Hz.
    psd : numpy.ndarray
        Power spectral density in strain²/Hz.
    """

    frequencies, psd = welch(
        strain,
        fs=sampling_rate
    )

    return frequencies, psd

def main():
    # Load your LIGO data
    from waveprocessing.data.reading import load_strain

    FILE = "data/raw/GW150914_H1.hdf5"

    strain, sampling_rate = load_strain(FILE)

    # Calculate P
    frequencies, psd = calculate_psd(
        strain,
        sampling_rate
    )

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