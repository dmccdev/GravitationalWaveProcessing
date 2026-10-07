import h5py

FILE = "data/raw/GW150914_H1.hdf5"

def load_strain(path: str) -> tuple:
    with h5py.File(path, "r") as f:
        strain = f["strain/Strain"][:]
        duration = f["meta/Duration"][()]

    sampling_rate = len(strain) / duration

    return strain, sampling_rate

if __name__ == "__main__":
    strain, sampling_rate = load_strain(FILE)
    print("Calculated Sampling rate is: ", sampling_rate, " Hz") #4096.0Hz
    print("Strain is: ", strain) #A long 1dim array