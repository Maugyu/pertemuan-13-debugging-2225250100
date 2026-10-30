# Praktik 4: Investigasi dan Perbaikan Bug
# Pertemuan 13 - Algoritma dan Pemrograman

def hitung_rata_rata(nilai):
    if not nilai:
        raise ValueError("Data nilai tidak boleh kosong.")

    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"

    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if not nilai:
        raise ValueError("Data nilai tidak boleh kosong.")

    tertinggi = nilai[0]

    for x in nilai:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


# Data utama
nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Pengujian otomatis
def jalankan_test():
    test_case = [
        ("T1", hitung_rata_rata, [80, 60, 90, 70], 75.0),
        ("T2", hitung_rata_rata, [100, 80], 90.0),
        ("T3", status, 60, "Lulus"),
        ("T4", status, 59, "Tidak lulus"),
        ("T5", nilai_tertinggi, [80, 60, 90, 70], 90),
    ]

    semua_lulus = True

    print("\n=== HASIL PENGUJIAN ===")

    for test_id, fungsi, data, expected in test_case:
        actual = fungsi(data)

        if actual == expected:
            hasil = "PASS"
        else:
            hasil = "FAIL"
            semua_lulus = False

        print(
            f"{test_id} | Expected: {expected} | "
            f"Actual: {actual} | {hasil}"
        )

    # Test tambahan: rata-rata dengan tiga nilai
    actual = hitung_rata_rata([80, 90, 70])
    expected = 80.0

    if actual == expected:
        print("T6 | Rata-rata tiga nilai | PASS")
    else:
        print(
            f"T6 | Expected: {expected} | "
            f"Actual: {actual} | FAIL"
        )
        semua_lulus = False

    # Test tambahan: list kosong
    for nama_fungsi, fungsi in [
        ("rata-rata", hitung_rata_rata),
        ("nilai tertinggi", nilai_tertinggi),
    ]:
        try:
            fungsi([])
            print(f"T7 | {nama_fungsi} data kosong | FAIL")
            semua_lulus = False
        except ValueError:
            print(f"T7 | {nama_fungsi} data kosong | PASS")

    if semua_lulus:
        print("\nSemua test berhasil.")
    else:
        print("\nMasih terdapat test yang gagal.")


if __name__ == "__main__":
    jalankan_test()