"""Fungsi tampilan dan penyusunan laporan."""


def format_laporan(statistik, ketuntasan, data):
    """Menyusun laporan dengan format yang konsisten."""
    garis = "=" * 52
    baris = [
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
        status = "Tuntas" if siswa["nilai"] >= ketuntasan["kkm"] else "Belum Tuntas"
        baris.append(f"{siswa['nama']:<20} {siswa['nilai']:>6.2f}  {status}")
    baris.append(garis)
    return "\n".join(baris) + "\n"


def tampilkan_header():
    print("=" * 52)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS")
    print("=" * 52)
