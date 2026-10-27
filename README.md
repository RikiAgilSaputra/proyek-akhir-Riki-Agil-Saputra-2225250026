# Program Rekap dan Analisis Nilai Matematika Kelas

## Deskripsi
Program terminal membaca data siswa dari file teks, memvalidasi nilai pada rentang 0-100, menghitung statistik kelas, menentukan ketuntasan berdasarkan KKM, menampilkan hasil, dan menyimpan laporan.

## Fitur
- Membaca file berformat `Nama|Nilai`.
- Mengabaikan baris kosong dan komentar yang diawali `#`.
- Memeriksa format, nama, nilai numerik, serta rentang nilai 0-100.
- Menghitung jumlah data, rata-rata, minimum, dan maksimum.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menampilkan serta menyimpan laporan.

## Persyaratan
Python 3.x. Tidak memerlukan pustaka eksternal.

## Cara Menjalankan
Jalankan dari folder utama proyek:

```bash
python main.py
```

Jangan menjalankan `main.py` dari folder `src`, karena jalur file input relatif terhadap folder utama.

## Konfigurasi
- File input: `data/nilai_contoh.txt`
- File output: `output/laporan_nilai.txt`
- KKM: `75`

## Struktur Folder
```text
proyek_analisis_nilai_diselaraskan/
|-- README.md
|-- main.py
|-- data/
|   `-- nilai_contoh.txt
|-- src/
|   |-- analisis.py
|   |-- data_io.py
|   `-- utilitas.py
|-- tests/
|   `-- test_case.md
`-- output/
    `-- .gitkeep
```

## Catatan batasan materi: tanpa import
Agar sesuai batasan materi yang belum memperbolehkan `import`, `main.py` berisi fungsi yang diperlukan sehingga dapat dijalankan secara mandiri. File di `src/` menyimpan versi fungsi yang dipisahkan berdasarkan tanggung jawab sebagai rancangan modular dan referensi pengembangan. Python tidak menyediakan pemanggilan fungsi antar-file `.py` secara normal tanpa mekanisme penghubung seperti `import`; karena itu, `main.py` belum memanggil fungsi di `src/`. Jika materi `import` sudah diperbolehkan, fungsi-fungsi dapat dipindahkan menjadi modul yang benar-benar dipakai bersama, tanpa duplikasi.

## Pengujian
Lihat `tests/test_case.md`. Setelah menjalankan program, periksa laporan di `output/laporan_nilai.txt`.

## Batasan
Program menggunakan antarmuka terminal, file teks, fungsi, list, dictionary, perulangan, seleksi, dan penanganan error dasar. Tidak memakai GUI, web, atau pustaka eksternal.
