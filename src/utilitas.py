def tampilkan_hasil(hasil):
    if hasil is None:
        print("Tidak ada data nilai yang valid.")
        return

    print("\n=== HASIL ANALISIS NILAI ===")
    print(f"Jumlah siswa : {hasil['jumlah']}")
    print(f"Rata-rata    : {hasil['rata_rata']:.2f}")
    print(f"Nilai minimum: {hasil['minimum']:.2f}")
    print(f"Nilai maksimum: {hasil['maksimum']:.2f}")
    print("\nDaftar siswa:")

    for siswa in hasil["status"]:
        print(
            f"{siswa['nama']}: {siswa['nilai']:.2f} "
            f"- {siswa['status']}"
        )
