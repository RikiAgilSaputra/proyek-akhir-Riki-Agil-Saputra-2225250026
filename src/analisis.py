"""Logika validasi, statistik, dan ketuntasan nilai."""


def validasi_nilai(nilai):
    """Nilai valid berada pada rentang inklusif 0-100."""
    return 0 <= nilai <= 100


def filter_data_valid(data):
    """Mengembalikan data siswa yang nilainya valid."""
    return [siswa for siswa in data if validasi_nilai(siswa["nilai"])]


def hitung_statistik(data):
    """Mengembalikan statistik atau None jika data kosong."""
    if not data:
        return None
    nilai = [siswa["nilai"] for siswa in data]
    return {
        "jumlah_data": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
    }


def tentukan_status(nilai, kkm):
    """Menghasilkan Tuntas atau Belum Tuntas."""
    return "Tuntas" if nilai >= kkm else "Belum Tuntas"


def rekap_ketuntasan(data, kkm):
    """Menghitung jumlah siswa menurut status ketuntasan."""
    tuntas = sum(1 for siswa in data if tentukan_status(siswa["nilai"], kkm) == "Tuntas")
    return {"kkm": kkm, "tuntas": tuntas, "belum_tuntas": len(data) - tuntas}
