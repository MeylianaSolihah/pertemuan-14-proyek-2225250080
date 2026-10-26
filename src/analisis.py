def analisis_nilai(data, batas_tuntas=75):
    if not data:
        return None

    nilai = [siswa["nilai"] for siswa in data]
    return {
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "jumlah": len(nilai),
        "status": [
            {
                "nama": siswa["nama"],
                "nilai": siswa["nilai"],
                "status": "Tuntas" if siswa["nilai"] >= batas_tuntas else "Belum tuntas",
            }
            for siswa in data
        ],
    }
