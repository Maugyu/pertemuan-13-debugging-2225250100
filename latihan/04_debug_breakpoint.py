# Latihan 4: Debugging Menggunakan Breakpoint

def hitung_rata_rata(data):
    if not data:
        return 0

    total = sum(data)
    jumlah_data = len(data)

    return total / jumlah_data


data = [80, 90, 70]

hasil = hitung_rata_rata(data)

print("Data:", data)
print("Jumlah data:", len(data))
print("Rata-rata:", hasil)