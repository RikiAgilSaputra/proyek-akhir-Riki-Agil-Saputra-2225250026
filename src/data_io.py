"""Fungsi pembacaan data dan penyimpanan laporan."""


def baca_data(file_input):
    """Membaca Nama|Nilai; baris bermasalah dilewati dengan peringatan."""
    data = []
    with open(file_input, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue
            bagian = baris.split("|")
            if len(bagian) != 2:
                print(f"Peringatan baris {nomor_baris}: format harus Nama|Nilai.")
                continue
            nama = bagian[0].strip()
            teks_nilai = bagian[1].strip()
            if not nama:
                print(f"Peringatan baris {nomor_baris}: nama kosong.")
                continue
            try:
                nilai = float(teks_nilai)
            except ValueError:
                print(f"Peringatan baris {nomor_baris}: nilai harus angka.")
                continue
            if not 0 <= nilai <= 100:
                print(f"Peringatan baris {nomor_baris}: nilai harus 0-100.")
                continue
            data.append({"nama": nama, "nilai": nilai})
    return data


def simpan_laporan(teks_laporan, file_output):
    """Menulis teks laporan ke file output."""
    with open(file_output, "w", encoding="utf-8") as file:
        file.write(teks_laporan)
