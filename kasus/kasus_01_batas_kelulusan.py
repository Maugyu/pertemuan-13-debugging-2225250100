# Kasus 1: Bug Batas Kelulusan

def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


# Test case
test_case = [59, 60, 61]

for nilai in test_case:
    print(f"Nilai: {nilai} -> {status_lulus(nilai)}")