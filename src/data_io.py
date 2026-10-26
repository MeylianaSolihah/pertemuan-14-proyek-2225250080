from pathlib import Path


def baca_data_nilai(nama_file="data/nilai_contoh.txt"):
    """Membaca data nama dan nilai siswa dari file teks."""
    path_file = Path(nama_file)

    if not path_file.exists():
        print(f"File tidak ditemukan: {nama_file}")
        return []

    data_nilai = []

    try:
        with path_file.open("r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Format data salah pada baris {nomor_baris}.")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Nilai tidak valid pada baris {nomor_baris}.")
                    continue

                if not nama:
                    print(f"Nama kosong pada baris {nomor_baris}.")
                    continue

                if nilai < 0 or nilai > 100:
                    print(f"Nilai harus 0-100 pada baris {nomor_baris}.")
                    continue

                data_nilai.append({"nama": nama, "nilai": nilai})

    except OSError as error:
        print(f"Gagal membaca file: {error}")
        return []

    return data_nilai
