def analisis_nilai(data_nilai, kkm=75):
    """Menghitung statistik nilai dan jumlah kelulusan."""
    if not data_nilai:
        return {
            "rata_rata": 0,
            "nilai_tertinggi": None,
            "nilai_terendah": None,
            "jumlah_lulus": 0,
            "jumlah_tidak_lulus": 0,
        }

    daftar_nilai = [siswa["nilai"] for siswa in data_nilai]

    jumlah_lulus = sum(1 for nilai in daftar_nilai if nilai >= kkm)
    jumlah_tidak_lulus = len(daftar_nilai) - jumlah_lulus

    return {
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "nilai_tertinggi": max(daftar_nilai),
        "nilai_terendah": min(daftar_nilai),
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": jumlah_tidak_lulus,
    }
