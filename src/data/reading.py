import h5py

FILE = "data/raw/GW150914_H1.hdf5"

with h5py.File(FILE, "r") as f:
    strain = f["strain/Strain"]
    duration = f["meta/Duration"][()]

    sampling_rate = len(strain) / duration
    print(sampling_rate, "Hz") #4096Hz