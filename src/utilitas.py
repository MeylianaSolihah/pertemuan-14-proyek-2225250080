from pathlib import Path


def tampilkan_laporan(data_nilai, hasil_analisis, kkm=75):
    """Menampilkan rekap nilai siswa ke terminal."""
    print("\n=== REKAP DAN ANALISIS NILAI MATEMATIKA ===")
    print(f"KKM: {kkm}")
    print("-" * 40)

    for nomor, siswa in enumerate(data_nilai, start=1):
        status = "Lulus" if siswa["nilai"] >= kkm else "Tidak lulus"
        print(f"{nomor}. {siswa['nama']}: {siswa['nilai']:g} - {status}")

    print("-" * 40)
    print(f"Rata-rata       : {hasil_analisis['rata_rata']:.2f}")
    print(f"Nilai tertinggi : {hasil_analisis['nilai_tertinggi']}")
    print(f"Nilai terendah  : {hasil_analisis['nilai_terendah']}")
    print(f"Jumlah lulus    : {hasil_analisis['jumlah_lulus']}")
    print(f"Jumlah tidak lulus: {hasil_analisis['jumlah_tidak_lulus']}")


def simpan_laporan(data_nilai, hasil_analisis, kkm=75,
                   nama_file="output/laporan_nilai.txt"):
    """Menyimpan rekap nilai ke file teks."""
    path_file = Path(nama_file)

    try:
        path_file.parent.mkdir(parents=True, exist_ok=True)

        with path_file.open("w", encoding="utf-8") as file:
            file.write("REKAP DAN ANALISIS NILAI MATEMATIKA\n")
            file.write(f"KKM: {kkm}\n\n")

            for siswa in data_nilai:
                status = "Lulus" if siswa["nilai"] >= kkm else "Tidak lulus"
                file.write(
                    f"{siswa['nama']}: {siswa['nilai']:g} - {status}\n"
                )

            file.write("\nRINGKASAN\n")
            file.write(f"Rata-rata: {hasil_analisis['rata_rata']:.2f}\n")
            file.write(f"Nilai tertinggi: {hasil_analisis['nilai_tertinggi']}\n")
            file.write(f"Nilai terendah: {hasil_analisis['nilai_terendah']}\n")
            file.write(f"Jumlah lulus: {hasil_analisis['jumlah_lulus']}\n")
            file.write(
                f"Jumlah tidak lulus: "
                f"{hasil_analisis['jumlah_tidak_lulus']}\n"
            )

        print(f"Laporan berhasil disimpan di: {path_file}")
        return True

    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False
