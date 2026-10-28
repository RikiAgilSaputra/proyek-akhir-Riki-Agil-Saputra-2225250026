# Test Case - Pertemuan 14

Jumlah skenario: 7, yaitu lima kasus minimum dan dua kasus tambahan. ID, kategori, dan kondisi disamakan dengan test case Pertemuan 15. Hasil yang diharapkan di bawah ini mengikuti perilaku program Pertemuan 14. Karena file ini merupakan rancangan pengujian, kolom hasil aktual dan status belum diisi.

| ID | Kategori | Input/kondisi | Hasil yang diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Jumlah 3; rata-rata 80.00; minimum 70; maksimum 90; tuntas 2; belum tuntas 1 |
| TC02 | Boundary | Nilai 0 dan 100 | Keduanya diterima sebagai data valid; rata-rata 50.00; minimum 0; maksimum 100 |
| TC03 | Boundary KKM | Nilai 75 dan 74 dengan KKM 75 | Nilai 75 berstatus Tuntas; nilai 74 berstatus Belum Tuntas; jumlah tuntas 1 dan belum tuntas 1 |
| TC04 | Invalid | Baris format salah, nama kosong, nilai `abc`, `-1`, dan `101` | Lima peringatan sesuai jenis kesalahan; semua baris dilewati; karena tidak ada data valid, program menampilkan pesan data valid tidak tersedia dan berhenti tanpa menghitung rata-rata atau menyimpan laporan |
| TC05 | Empty | File hanya berisi komentar dan baris kosong | Pesan tidak ada data siswa valid; tidak terjadi pembagian nol; program berhenti sebelum menyusun atau menyimpan laporan |
| TC06 | File input | File input tidak ditemukan | Pesan kesalahan file input ditampilkan; program berhenti dengan aman |
| TC07 | File output | Folder `output/` tidak tersedia, dengan data contoh normal | Laporan analisis ditampilkan; pesan kesalahan penyimpanan karena file/folder tujuan tidak ditemukan |

## Hasil yang diharapkan untuk data contoh

File `data/nilai_contoh.txt` menghasilkan 10 data valid, rata-rata 70.70, minimum 0, maksimum 100, 5 siswa tuntas, dan 5 siswa belum tuntas.