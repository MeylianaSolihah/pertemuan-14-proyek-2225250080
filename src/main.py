from data_io import baca_data_nilai
from analisis import analisis_nilai
from utilitas import tampilkan_laporan, simpan_laporan


def main():
    kkm = 75
    data_nilai = baca_data_nilai()

    if not data_nilai:
        print("Tidak ada data nilai yang dapat dianalisis.")
        return

    hasil = analisis_nilai(data_nilai, kkm)

    tampilkan_laporan(data_nilai, hasil, kkm)
    simpan_laporan(data_nilai, hasil, kkm)


if __name__ == "__main__":
    main()
