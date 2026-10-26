# PROPOSAL PROYEK
## Program Rekap dan Analisis Nilai Matematika Kelas

### 1. Latar Belakang
Pengolahan nilai matematika siswa secara manual membutuhkan waktu dan berisiko menimbulkan kesalahan. Oleh karena itu, diperlukan program sederhana untuk membantu membaca, mengolah, dan menganalisis nilai siswa menggunakan Python.

### 2. Pengguna dan Tujuan
**Pengguna:** Guru atau pihak yang membutuhkan rekap nilai siswa.

**Tujuan:** Mempermudah pengolahan nilai, perhitungan statistik, penentuan ketuntasan, dan pembuatan laporan nilai.

### 3. Ruang Lingkup dan Batasan
Program berbasis terminal ini memiliki ruang lingkup:
- Membaca data nama dan nilai siswa dari file teks.
- Memvalidasi data dan nilai pada rentang 0–100.
- Menghitung rata-rata, nilai minimum, dan maksimum.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menampilkan dan menyimpan laporan analisis ke file teks.

Batasan:
- Data dibaca dari file teks dengan format nama,nilai.
- KKM yang digunakan adalah 75.
- Program tidak menggunakan antarmuka grafis atau web.

### 4. Kebutuhan Fungsional
1. Program dapat membaca data nilai dari file.
2. Program memeriksa format data dan rentang nilai.
3. Program mengabaikan data yang tidak valid serta menampilkan pemberitahuan.
4. Program menghitung statistik nilai siswa yang valid.
5. Program menentukan ketuntasan berdasarkan KKM 75.
6. Program menampilkan hasil dan menyimpan laporan dalam file teks.

### 5. Input, Proses, dan Output (IPO)

**Input:**
- File teks berisi nama dan nilai siswa.

**Proses:**
- Membaca data.
- Memvalidasi nama dan nilai.
- Menghitung rata-rata, nilai minimum, dan maksimum.
- Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM 75.
- Menyusun laporan hasil analisis.

**Output:**
- Daftar nilai siswa dan status ketuntasan.
- Rata-rata, nilai minimum, dan maksimum.
- Jumlah siswa tuntas dan belum tuntas.
- File laporan hasil analisis.

### 6. Algoritma atau Pseudocode
MULAI
1. Tentukan lokasi file data nilai.
2. Baca data dari file.
3. Periksa setiap baris data.
4. Jika format, nama, atau nilai tidak valid, abaikan data tersebut.
5. Jika valid, simpan data siswa.
6. Jika tidak ada data valid, tampilkan pesan.
7. Jika ada data valid:
   a. Hitung rata-rata, nilai minimum, dan maksimum.
   b. Hitung jumlah siswa tuntas dan belum tuntas.
   c. Tampilkan hasil analisis.
   d. Simpan hasil ke file laporan teks.
8. Selesai.

### 7. Struktur Program
- `src/main.py`: menjalankan alur utama program.
- `src/data_io.py`: membaca dan memvalidasi data.
- `src/analisis.py`: menghitung statistik dan ketuntasan.
- `src/utilitas.py`: membantu menampilkan dan menyimpan laporan.

### 8. Struktur Data
Data siswa disimpan dalam list yang berisi dictionary. Setiap dictionary memiliki kunci `nama` dan `nilai`.

Contoh:
`{"nama": "Ani", "nilai": 80}`

List digunakan untuk menyimpan banyak siswa, sedangkan dictionary menyimpan informasi setiap siswa.

### 9. Rencana Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | Nilai berupa teks abc | Ditolak dengan pesan validasi |
| TC06 | Invalid | File tidak ditemukan | Kesalahan ditangani dan pesan ditampilkan |
| TC07 | Normal | Semua nilai minimal 75 | Semua siswa berstatus tuntas |
| TC08 | Normal | Data nilai valid tersedia | Laporan disimpan ke file teks |

### 10. Pembagian Tugas
Pembagian berikut merupakan rancangan awal dan perlu disesuaikan dengan anggota tim.

- Koordinator: mengawasi ruang lingkup dan integrasi proyek.
- Programmer Data I/O: menangani pembacaan file dan validasi data.
- Programmer Logika: menangani statistik dan ketuntasan.
- Tester/QA: menyiapkan serta memeriksa test case.
- Dokumentasi: menyusun README dan proposal.

Jika proyek dikerjakan sendiri, seluruh peran dapat dilakukan oleh satu orang.

### 11. Jadwal dan Milestone
- Pertemuan 14: menyelesaikan proposal, struktur folder, pseudocode, test case, dan pembagian tugas.
- Antara Pertemuan 14–15: menyiapkan implementasi awal fitur wajib.
- Pertemuan 15: integrasi program, pengujian, debugging, dan dokumentasi.
- Pertemuan 16: menyelesaikan perbaikan dan persiapan hasil akhir sesuai arahan dosen.

### 12. Repositori GitHub
URL repositori: Diisi setelah repositori GitHub dibuat.

### 13. Catatan
Proposal ini menjadi rancangan awal untuk implementasi dan pengujian program pada tahap berikutnya.
