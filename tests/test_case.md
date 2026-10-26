# Test Case Program Rekap dan Analisis Nilai

| ID | Skenario | Data/Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Data normal | Nilai 80, 70, 90 | Rata-rata 80 dan nilai berhasil dianalisis |
| TC02 | Nilai batas bawah | Nilai 0 | Nilai diterima |
| TC03 | Nilai batas atas | Nilai 100 | Nilai diterima |
| TC04 | Nilai melebihi batas | Nilai 105 | Data ditolak |
| TC05 | Nilai bukan angka | Nilai abc | Data ditolak |
| TC06 | File tidak ditemukan | File data tidak tersedia | Program menampilkan pesan dan berhenti dari proses analisis |
| TC07 | Pemeriksaan kelulusan | Nilai 75 dengan KKM 75 | Siswa dinyatakan lulus |
| TC08 | Penyimpanan laporan | Data berhasil dianalisis | Laporan tersimpan di output/laporan_nilai.txt |

## Catatan
Pengujian dilakukan untuk memastikan program dapat membaca data, memvalidasi nilai, menghitung statistik, menentukan kelulusan, dan menyimpan laporan.
