# PROPOSAL PROYEK
## Program Rekap dan Analisis Nilai Matematika Kelas

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa  
**Pertemuan:** 14 – Perancangan Proyek Program Sederhana  
**Tahun Ajaran:** 2026/2027 Ganjil

## 1. Latar Belakang

Rekap nilai siswa secara manual membutuhkan waktu dan berpotensi menimbulkan kesalahan. Program ini membantu guru merekap nilai secara otomatis dengan konsep dasar Python.

## 2. Tujuan

1. Membaca data nama dan nilai dari file teks.
2. Memvalidasi format data, nama, serta nilai pada rentang 0–100.
3. Menghitung jumlah data, rata-rata, minimum, dan maksimum.
4. Menentukan status tuntas berdasarkan Kriteria Ketuntasan Minimal (KKM).
5. Menghitung jumlah siswa tuntas dan belum tuntas.
6. Menampilkan dan menyimpan laporan teks.

## 3. Ruang Lingkup dan Batasan Materi

Program berjalan di terminal dan menggunakan file teks lokal. Implementasi utama sengaja tidak menggunakan `import` karena belum termasuk materi yang diperbolehkan pada tahap ini.

Konsep yang digunakan:
- variabel dan tipe data dasar;
- string, list, dan dictionary;
- operator;
- percabangan `if/else`;
- perulangan `for`;
- fungsi `def` dan `return`;
- file handling dengan `open`;
- penanganan error dasar dengan `try/except`.

Program tidak menggunakan GUI, web, pustaka eksternal, atau mekanisme impor antarmodul. Program juga tidak menggunakan class, lambda, decorator, list comprehension, `pathlib`, `os`, maupun modul statistik.

File di dalam folder `src/` berfungsi sebagai rancangan modular dan referensi pengembangan. Karena materi `import` belum diperbolehkan, `main.py` memuat fungsi yang diperlukan agar dapat dijalankan secara mandiri dan tidak memanggil fungsi dari file di `src/`. Dengan demikian, fungsi di `src/` dan `main.py` dapat memiliki isi yang serupa, tetapi memiliki peran dokumentasi/pengembangan yang berbeda.

## 4. Kebutuhan Fungsional

| ID | Kebutuhan |
|---|---|
| F01 | Membaca data dari `data/nilai_contoh.txt` dengan format `Nama|Nilai` |
| F02 | Mengabaikan baris kosong dan baris komentar yang diawali `#` |
| F03 | Memeriksa format data, menolak nama kosong, nilai nonnumerik, dan nilai di luar rentang 0–100 |
| F04 | Menghitung jumlah data valid, rata-rata, nilai minimum, dan nilai maksimum |
| F05 | Menentukan status tuntas jika nilai >= KKM, dengan KKM sebesar 75 |
| F06 | Menghitung jumlah siswa tuntas dan belum tuntas |
| F07 | Menampilkan laporan di terminal dan menyimpannya ke `output/laporan_nilai.txt` |

## 5. Input, Proses, dan Output

| Komponen | Spesifikasi |
|---|---|
| Input | `data/nilai_contoh.txt` |
| Format | `Nama|Nilai` |
| Baris yang diabaikan | Baris kosong dan komentar yang diawali `#` |
| Validasi | Format harus benar, nama tidak boleh kosong, nilai harus numerik dan berada pada rentang 0–100 |
| KKM | `75` |
| Proses | Baca file → abaikan baris kosong/komentar → periksa format → validasi → simpan data valid → hitung statistik → tentukan status → susun laporan |
| Output terminal | Statistik kelas dan detail status setiap siswa |
| Output file | `output/laporan_nilai.txt` |

## 6. Pseudocode

```text
MULAI
  tentukan file input, file output, dan KKM = 75
  coba buka dan baca file input
  jika file tidak ditemukan:
    tampilkan pesan error
    SELESAI

  untuk setiap baris:
    hapus spasi di awal dan akhir
    jika baris kosong atau diawali "#":
      lanjutkan
    pisahkan baris berdasarkan "|"
    jika format salah atau nama kosong:
      tampilkan peringatan
      lanjutkan
    coba ubah nilai menjadi angka
    jika konversi gagal karena nilai bukan angka:
      tampilkan peringatan
      lanjutkan
    jika nilai di luar 0–100:
      tampilkan peringatan
      lanjutkan
    simpan nama dan nilai sebagai data valid

  jika tidak ada data valid:
    tampilkan pesan bahwa data valid tidak tersedia
    SELESAI

  hitung jumlah data, rata-rata, minimum, dan maksimum
  tentukan status setiap siswa berdasarkan KKM
  hitung jumlah siswa tuntas dan belum tuntas
  susun laporan
  tampilkan laporan di terminal
  coba simpan laporan ke file output
  jika file atau folder tujuan tidak ditemukan:
    tampilkan pesan error
SELESAI
```

## 7. Struktur Program

Titik masuk program berada di `src/main.py`. Jalankan dari folder utama dengan `python src/main.py`, karena jalur file input dan output relatif terhadap folder utama. Sesuai batasan materi, `src/main.py` berjalan mandiri tanpa `import`; berkas lain di `src/` menyimpan fungsi yang dipisahkan berdasarkan tanggung jawab sebagai rancangan/referensi dan belum dipanggil oleh titik masuk.

~~~text
proyek-akhir-Riki Agil Saputra-2225250026/
├── .gitignore
├── README.md
├── proposal.md
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
~~~
## 8. Struktur Data

Data siswa disimpan dalam list berisi dictionary:

```python
[
    {"nama": "Ayu", "nilai": 85.0},
    {"nama": "Budi", "nilai": 78.0}
]
```

List menampung kumpulan siswa, sedangkan setiap dictionary menyimpan nama dan nilai. Nilai disimpan sebagai angka agar dapat digunakan dalam perhitungan statistik dan penentuan status ketuntasan.

## 9. Test Case

Rancangan pada `tests/test_case.md` memakai tujuh ID, kategori, dan kondisi yang sama dengan Pertemuan 15: normal, batas nilai, batas KKM, data tidak valid, data kosong, file input tidak ditemukan, dan file output tidak ditemukan. Hasil yang diharapkan mengikuti implementasi Pertemuan 14. Pada tahap ini, kasus tanpa data valid berhenti setelah menampilkan pesan; penyusunan dan penyimpanan laporan kosong menjadi peningkatan pada Pertemuan 15.

## 10. Kriteria Selesai

- Semua fitur wajib berjalan sesuai deskripsi pada README.
- `src/main.py` dapat dijalankan dari folder utama menggunakan `python src/main.py`.
- Implementasi utama tidak memakai `import`.
- Baris kosong dan komentar yang diawali `#` diabaikan.
- Format, nama, dan nilai divalidasi sesuai ketentuan.
- Statistik kelas dan status ketuntasan sesuai data valid serta KKM 75.
- Error dasar ditangani.
- Laporan ditampilkan di terminal dan disimpan ke `output/laporan_nilai.txt`.
- Struktur folder sesuai dengan README.
- Anggota kelompok memahami alur program, fungsi-fungsinya, dan hasil pengujian.

## 11. Pembagian Tugas

| Peran | Tanggung jawab |
|---|---|
| Koordinator | Mengatur integrasi dan ruang lingkup proyek |
| Programmer | Mengimplementasikan fungsi yang diperlukan dalam `main.py` serta menjaga kesesuaiannya dengan rancangan fungsi di `src/` |
| Tester/QA | Menjalankan pengujian manual berdasarkan `tests/test_case.md` dan memeriksa laporan keluaran |
| Dokumentasi | Memelihara proposal dan README agar menjelaskan struktur serta cara menjalankan program dengan konsisten |

Sesuaikan peran dengan jumlah anggota kelompok.

## 12. Jadwal dan Milestone

| Waktu | Target |
|---|---|
| Pertemuan 14 | Proposal, struktur proyek, pseudocode, test case awal, dan pembagian tugas |
| Antara Pertemuan 14–15 | Implementasi awal fitur wajib |
| Pertemuan 15 | Integrasi, pengujian, debugging, dan dokumentasi |
| Pertemuan 16 | Presentasi, demonstrasi, dan evaluasi proyek |

## 13. Repository GitHub

URL Remote yang tercatat pada konfigurasi Git proyek: https://github.com/RikiAgilSaputra/proyek-akhir-Riki-Agil-Saputra-2225250026. 
## 14. Integritas Akademik

Setiap anggota kelompok perlu memahami algoritma, struktur program, hasil pengujian, dan kontribusinya sendiri serta mengikuti kebijakan mata kuliah.

