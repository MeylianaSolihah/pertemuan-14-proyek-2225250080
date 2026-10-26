from pathlib import Path
from data_io import baca_data
from analisis import analisis_nilai
from utilitas import tampilkan_hasil


def main():
    folder_proyek = Path(__file__).resolve().parent.parent
    lokasi_data = folder_proyek / "data" / "nilai_contoh.txt"

    data = baca_data(lokasi_data)
    hasil = analisis_nilai(data)
    tampilkan_hasil(hasil)


if __name__ == "__main__":
    main()
