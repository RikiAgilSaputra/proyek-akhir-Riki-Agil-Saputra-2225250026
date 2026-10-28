# Program Rekap dan Analisis Nilai Matematika Kelas

## Deskripsi

Program terminal membaca data siswa dari file teks, memvalidasi nama dan nilai pada rentang 0–100, menghitung statistik kelas, menentukan ketuntasan berdasarkan KKM, lalu menampilkan dan menyimpan laporan.

## Fitur

- Membaca file berformat `Nama|Nilai`.
- Mengabaikan baris kosong dan komentar yang diawali `#`.
- Memeriksa format, nama, nilai numerik, serta rentang nilai 0–100.
- Menghitung jumlah data, rata-rata, minimum, dan maksimum.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menampilkan serta menyimpan laporan.

## Persyaratan

Python 3.x. Tidak memerlukan pustaka eksternal.

## Cara Menjalankan

Buka terminal pada folder utama proyek dan jalankan:

~~~bash
python src/main.py
~~~

Jalankan perintah tersebut dari folder utama karena jalur input dan output dihitung relatif terhadap folder itu.

## Konfigurasi

- File input: `data/nilai_contoh.txt`
- File output: `output/laporan_nilai.txt`
- KKM: `75`

## Struktur Folder

~~~text
.
├── .gitignore
├── README.md
├── proposal.md
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── analisis.py
│   ├── data_io.py
│   ├── main.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    ├── .gitkeep
    └── laporan_nilai.txt
~~~

`src/main.py` adalah program mandiri tanpa `import`. Modul lain di `src/` berisi fungsi yang dipisahkan berdasarkan tanggung jawab, tetapi belum dipanggil oleh `src/main.py` karena batasan materi tanpa import.

## Pengujian

`tests/test_case.md` memuat 7 skenario rancangan dengan ID dan kondisi yang disamakan dengan Pertemuan 15. Jumlahnya lima kasus minimum ditambah dua kasus; hasil yang diharapkan disesuaikan dengan perilaku Pertemuan 14. Hasil aktual/status belum dicantumkan pada tahap rancangan ini.

## GitHub

Remote Git yang tercatat pada salinan ini adalah [proyek akhir Riki Agil Saputra](https://github.com/RikiAgilSaputra/proyek-akhir-Riki-Agil-Saputra-2225250026). Pastikan repositori dapat diakses sebelum pengumpulan.

## Batasan

Program memakai antarmuka terminal, file teks, fungsi, list, dictionary, perulangan, seleksi, dan penanganan error dasar. Program tidak memakai GUI, web, atau pustaka eksternal.
