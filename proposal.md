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
  jika file tidak ditemukan atau gagal dibaca:
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
    jika gagal:
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
  jika gagal:
    tampilkan pesan error
SELESAI
```

## 7. Struktur Program

Struktur proyek mengikuti README. `main.py` merupakan titik masuk program dan dapat dijalankan secara mandiri tanpa `import`. Folder `src/` menyimpan versi fungsi yang dipisahkan berdasarkan tanggung jawab sebagai rancangan modular dan referensi pengembangan, bukan sebagai modul yang dipanggil oleh `main.py` pada tahap ini.

```text
proyek_analisis_nilai_diselaraskan/
├── README.md
├── main.py
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── analisis.py
│   ├── data_io.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

Program dijalankan dari folder utama proyek dengan perintah:

```bash
python main.py
```

`main.py` tidak dijalankan dari folder `src/`, karena jalur file input menggunakan lokasi relatif terhadap folder utama proyek.

Konfigurasi yang digunakan:
- File input: `data/nilai_contoh.txt`
- File output: `output/laporan_nilai.txt`
- KKM: `75`

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

Pengujian dilakukan secara manual sesuai rincian pada `tests/test_case.md`. Kondisi yang diuji mencakup:
- data normal dengan format `Nama|Nilai`;
- baris kosong dan komentar yang diawali `#`;
- nilai batas 0 dan 100;
- nilai di bawah 0 atau di atas 100;
- nilai bukan angka;
- format baris salah dan nama kosong;
- file input tidak ditemukan atau gagal dibaca;
- tidak ada data valid;
- kegagalan penyimpanan laporan.

Setelah menjalankan program, hasil laporan dapat diperiksa di `output/laporan_nilai.txt`.

## 10. Kriteria Selesai

- Semua fitur wajib berjalan sesuai deskripsi pada README.
- `main.py` dapat dijalankan dari folder utama menggunakan `python main.py`.
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

## 12. Integritas Akademik

Setiap anggota kelompok perlu memahami algoritma, struktur program, hasil pengujian, dan kontribusinya sendiri serta mengikuti kebijakan mata kuliah.
