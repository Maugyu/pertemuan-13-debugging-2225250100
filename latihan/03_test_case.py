# Latihan 3: Test Case Batas Kelulusan

def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


# Test case sebelum perbaikan
test_case = [
    (59, "Tidak lulus"),
    (60, "Lulus"),
    (61, "Lulus"),
]

for nilai, expected in test_case:
    actual = status_lulus(nilai)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print(
        f"Nilai: {nilai} | "
        f"Expected: {expected} | "
        f"Actual: {actual} | "
        f"{status}"
    )
    