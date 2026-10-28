"""Program mandiri rekap dan analisis nilai matematika kelas."""

FILE_INPUT = "data/nilai_contoh.txt"
FILE_OUTPUT = "output/laporan_nilai.txt"
KKM = 75


def baca_data(file_input):
    """Membaca data Nama|Nilai dan melewati baris yang tidak valid."""
    data = []

    with open(file_input, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue

            bagian = baris.split("|")
            if len(bagian) != 2:
                print(
                    f"Peringatan baris {nomor_baris}: "
                    "format harus Nama|Nilai."
                )
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
                print(
                    f"Peringatan baris {nomor_baris}: "
                    "nilai harus berada pada rentang 0-100."
                )
                continue

            data.append({"nama": nama, "nilai": nilai})

    return data


def hitung_statistik(data):
    """Menghitung jumlah data, rata-rata, nilai minimum, dan maksimum."""
    if not data:
        return None

    jumlah_data = len(data)
    total_nilai = 0
    nilai_minimum = data[0]["nilai"]
    nilai_maksimum = data[0]["nilai"]

    for siswa in data:
        nilai = siswa["nilai"]
        total_nilai += nilai

        if nilai < nilai_minimum:
            nilai_minimum = nilai
        if nilai > nilai_maksimum:
            nilai_maksimum = nilai

    return {
        "jumlah_data": jumlah_data,
        "rata_rata": total_nilai / jumlah_data,
        "minimum": nilai_minimum,
        "maksimum": nilai_maksimum,
    }


def tentukan_status(nilai, kkm):
    """Menentukan status ketuntasan satu siswa."""
    if nilai >= kkm:
        return "Tuntas"
    return "Belum Tuntas"


def hitung_ketuntasan(data, kkm):
    """Menghitung jumlah siswa tuntas dan belum tuntas."""
    jumlah_tuntas = 0

    for siswa in data:
        if tentukan_status(siswa["nilai"], kkm) == "Tuntas":
            jumlah_tuntas += 1

    return {
        "kkm": kkm,
        "tuntas": jumlah_tuntas,
        "belum_tuntas": len(data) - jumlah_tuntas,
    }


def format_laporan(statistik, ketuntasan, data):
    """Menyusun ringkasan statistik dan status setiap siswa."""
    garis = "=" * 52
    baris_laporan = [
        garis,
        "LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA",
        garis,
        f"Jumlah data valid : {statistik['jumlah_data']}",
        f"Rata-rata         : {statistik['rata_rata']:.2f}",
        f"Nilai minimum     : {statistik['minimum']:.2f}",
        f"Nilai maksimum    : {statistik['maksimum']:.2f}",
        f"KKM               : {ketuntasan['kkm']}",
        f"Jumlah tuntas     : {ketuntasan['tuntas']}",
        f"Belum tuntas      : {ketuntasan['belum_tuntas']}",
        "",
        "DETAIL STATUS SISWA",
        "-" * 52,
    ]

    for siswa in data:
        status = tentukan_status(siswa["nilai"], ketuntasan["kkm"])
        baris_laporan.append(
            f"{siswa['nama']:<20} {siswa['nilai']:>6.2f}  {status}"
        )

    baris_laporan.append(garis)
    return "\n".join(baris_laporan) + "\n"


def main():
    """Menjalankan alur baca, analisis, dan pembuatan laporan."""
    print("=" * 52)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS")
    print("=" * 52)

    try:
        data = baca_data(FILE_INPUT)
    except FileNotFoundError as error:
        print(f"Gagal membaca file '{FILE_INPUT}': {error}")
        return

    if not data:
        print("Tidak ada data siswa valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data, KKM)
    laporan = format_laporan(statistik, ketuntasan, data)

    print(laporan, end="")

    try:
        with open(FILE_OUTPUT, "w", encoding="utf-8") as file:
            file.write(laporan)
    except FileNotFoundError as error:
        print(f"Gagal menyimpan laporan ke '{FILE_OUTPUT}': {error}")
        return

    print(f"Laporan tersimpan di '{FILE_OUTPUT}'.")


if __name__ == "__main__":
    main()