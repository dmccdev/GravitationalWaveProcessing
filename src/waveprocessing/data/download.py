from pathlib import Path
import requests


URL = ("https://gwosc.org/eventapi/json/GWTC-1-confident/GW150914/v3/H-H1_GWOSC_4KHZ_R1-1126259447-32.hdf5")
OUTPUT = Path("data/raw/GW150914_H1.hdf5")


def download_data() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading data to {OUTPUT}...")

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    OUTPUT.write_bytes(response.content)

    print("Download complete.")


if __name__ == "__main__":
    download_data()

