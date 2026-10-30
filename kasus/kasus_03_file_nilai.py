# Kasus 3: Bug Pengolahan File Nilai

def hitung_total_nilai(data):
    total = sum(data)
    return total


# Data yang dibaca dari file biasanya berbentuk string.
data_nilai = ["80", "90", "70"]

try:
    print("Total nilai:", hitung_total_nilai(data_nilai))
except TypeError as error:
    print("Terjadi kesalahan:", error)