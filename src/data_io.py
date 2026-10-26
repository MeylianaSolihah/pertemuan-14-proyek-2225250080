def baca_data(lokasi):
    data = []
    with open(lokasi, "r", encoding="utf-8-sig") as berkas:
        for nomor, baris in enumerate(berkas, start=1):
            baris = baris.strip()
            if not baris:
                continue

            bagian = baris.split(",")
            if len(bagian) != 2:
                print(f"Baris {nomor} dilewati: format tidak valid.")
                continue

            nama = bagian[0].strip()
            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor} dilewati: nilai bukan angka.")
                continue

            if not nama or not 0 <= nilai <= 100:
                print(f"Baris {nomor} dilewati: nama atau nilai tidak valid.")
                continue

            data.append({"nama": nama, "nilai": nilai})

    return data
