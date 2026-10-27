# Test Case - Program Rekap dan Analisis Nilai

| ID | Kategori | Input/kondisi | Hasil yang diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80.00 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Baris diabaikan dengan peringatan |
| TC05 | Invalid | Nilai berupa `abc` | Baris diabaikan dengan peringatan |
| TC06 | Invalid | Nama kosong | Baris diabaikan dengan peringatan |
| TC07 | File | File input tidak ditemukan | Pesan kesalahan ditampilkan, program berhenti dengan aman |
| TC08 | Ketuntasan | Nilai 75 dengan KKM 75 | Status Tuntas |
| TC09 | Ketuntasan | Nilai 74 dengan KKM 75 | Status Belum Tuntas |
| TC10 | Data | File berisi hanya komentar/baris kosong | Pesan tidak ada data valid; tidak terjadi pembagian nol |

## Hasil uji data contoh yang disediakan
- Jumlah siswa valid: 10
- Jumlah tuntas (nilai >= 75): 5
- Jumlah belum tuntas: 5
- Minimum: 0
- Maksimum: 100
- Rata-rata: 70.70

Kolom hasil aktual/status dapat diisi setelah setiap test case dijalankan.
