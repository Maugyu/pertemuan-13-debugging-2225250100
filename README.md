# Pertemuan 13 - Debugging dan Testing

**Nama:** Maulyditha Revania A.  
**NIM:** 2225250100  
**Kelas:** 3A

## 1. Tujuan Praktikum

Praktikum ini bertujuan untuk memahami proses debugging dan testing pada program Python. Kegiatan meliputi penelusuran alur program, penggunaan breakpoint, penyusunan test case, identifikasi bug, perbaikan kode, dan pengujian ulang untuk memastikan program berjalan sesuai harapan.

## 2. Struktur Folder

```text
pertemuan-13-debugging-2225250100/
├── README.md
├── .gitignore
├── kasus/
│   ├── kasus_01_batas_kelulusan.py
│   ├── kasus_02_rata_rata.py
│   └── kasus_03_file_nilai.py
├── latihan/
│   ├── 01_trace_loop.py
│   ├── 02_trace_fungsi.py
│   ├── 03_test_case.py
│   └── 04_debug_breakpoint.py
└── praktik/
    └── praktik_4_debugging.py
```

## 3. Kasus yang Diuji

Praktikum ini mencakup tiga kasus debugging dan empat latihan.

1. **Batas kelulusan:** Memperbaiki operator pembanding agar nilai 60 dinyatakan lulus.
2. **Perhitungan rata-rata:** Memperbaiki pembagi agar sesuai dengan jumlah data.
3. **Pengolahan file nilai:** Memperbaiki kesalahan tipe data string saat melakukan penjumlahan.
4. **Tracing perulangan:** Menelusuri perubahan nilai variabel pada setiap iterasi.
5. **Tracing fungsi:** Mengamati parameter, proses perhitungan, dan nilai pengembalian fungsi.
6. **Pengujian batas:** Menguji fungsi kelulusan menggunakan beberapa nilai.
7. **Breakpoint:** Memeriksa alur eksekusi dan nilai variabel melalui debugger VS Code.

## 4. Test Case

Test case digunakan untuk membandingkan hasil yang diharapkan (*expected result*) dengan hasil aktual (*actual result*).

### 4.1 Pengujian Sebelum Perbaikan

| ID | Fungsi | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|---|
| T1 | Rata-rata | `[80, 60, 90, 70]` | 75.0 | 60.0 | FAIL |
| T2 | Rata-rata | `[100, 80]` | 90.0 | 36.0 | FAIL |
| T3 | Status | `60` | Lulus | Tidak lulus | FAIL |
| T4 | Status | `59` | Tidak lulus | Tidak lulus | PASS |
| T5 | Nilai tertinggi | `[80, 60, 90, 70]` | 90 | 0 | FAIL |

### 4.2 Pengujian Setelah Perbaikan

| ID | Fungsi | Input | Expected | Actual | Status |
|---|---|---|---|---|---|
| T1 | Rata-rata | `[80, 60, 90, 70]` | 75.0 | 75.0 | PASS |
| T2 | Rata-rata | `[100, 80]` | 90.0 | 90.0 | PASS |
| T3 | Status | `60` | Lulus | Lulus | PASS |
| T4 | Status | `59` | Tidak lulus | Tidak lulus | PASS |
| T5 | Nilai tertinggi | `[80, 60, 90, 70]` | 90 | 90 | PASS |
| T6 | Rata-rata | `[80, 90, 70]` | 80.0 | 80.0 | PASS |
| T7 | List kosong | `[]` | ValueError | ValueError | PASS |

**Keterangan:** T7 menguji penanganan list kosong pada fungsi rata-rata dan nilai tertinggi. Kedua fungsi harus menghasilkan `ValueError` agar kesalahan dapat diketahui dengan jelas.

## 5. Bug Report

### Bug B01 - Perhitungan Rata-rata

- **Gejala:** Hasil rata-rata tidak sesuai dengan data.
- **Test case:** T1 dan T2.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Program menggunakan angka 5 sebagai pembagi tetap.
- **Perbaikan:** Mengganti pembagi dengan `len(nilai)` dan menambahkan pemeriksaan list kosong.
- **Retest:** PASS.

### Bug B02 - Status Kelulusan

- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Test case:** T3.
- **Lokasi:** Fungsi `status()`.
- **Akar penyebab:** Operator `>` tidak mencakup nilai yang sama dengan 60.
- **Perbaikan:** Mengubah operator `>` menjadi `>=`.
- **Retest:** PASS.

### Bug B03 - Nilai Tertinggi

- **Gejala:** Fungsi menghasilkan 0 meskipun terdapat nilai yang lebih tinggi.
- **Test case:** T5.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Variabel `tertinggi` diinisialisasi dengan 0 dan kondisi perbandingan menggunakan operator `<`.
- **Perbaikan:** Menginisialisasi `tertinggi` menggunakan elemen pertama dan mengganti operator `<` menjadi `>`.
- **Retest:** PASS.

### Bug B04 - Tipe Data Nilai

- **Gejala:** Program menghasilkan `TypeError` ketika menjumlahkan nilai berbentuk string.
- **Test case:** Data `["80", "90", "70"]`.
- **Lokasi:** Fungsi `hitung_total_nilai()`.
- **Akar penyebab:** Data belum dikonversi menjadi tipe numerik.
- **Perbaikan:** Mengonversi setiap nilai menggunakan `int()` sebelum menjumlahkannya.
- **Retest:** PASS.

## 6. Hasil Retest

Setelah perbaikan dilakukan, seluruh test case utama dijalankan kembali.

Hasil pengujian menunjukkan bahwa:

1. Perhitungan rata-rata sudah sesuai dengan jumlah data.
2. Nilai 60 dinyatakan lulus.
3. Fungsi nilai tertinggi menghasilkan nilai yang benar.
4. Data nilai berbentuk string dapat dikonversi sebelum dijumlahkan.
5. Program menangani list kosong dengan menghasilkan `ValueError`.
6. Seluruh test case yang telah ditentukan menghasilkan status PASS.

Dengan demikian, perbaikan berhasil mengatasi bug yang ditemukan pada program.

## 7. Cara Menjalankan Program

### Persyaratan

- Python telah terpasang.
- Visual Studio Code tersedia.
- Terminal dibuka pada direktori utama proyek.

### Menjalankan Program Praktik

```bash
python praktik/praktik_4_debugging.py
```

Jika perintah `python` tidak dikenali, gunakan:

```bash
py praktik/praktik_4_debugging.py
```

### Menjalankan Program Latihan

Contoh menjalankan latihan tracing perulangan:

```bash
python latihan/01_trace_loop.py
```

Contoh menjalankan latihan tracing fungsi:

```bash
python latihan/02_trace_fungsi.py
```

Contoh menjalankan pengujian batas kelulusan:

```bash
python latihan/03_test_case.py
```

Contoh menjalankan latihan breakpoint:

```bash
python latihan/04_debug_breakpoint.py
```

## Refleksi

Teknik debugging yang paling membantu adalah tracing dan breakpoint karena keduanya memungkinkan pemeriksaan alur program dan perubahan nilai variabel secara bertahap. Penggunaan test case juga membantu menemukan kesalahan yang tidak selalu terlihat hanya dengan membaca kode.

Melalui praktikum ini, saya memahami bahwa debugging bukan hanya mencari lokasi kesalahan, tetapi juga menemukan akar penyebabnya, memperbaiki kode, dan membuktikan bahwa perbaikan berhasil melalui pengujian ulang. Riwayat commit Git membantu mendokumentasikan setiap tahap pengerjaan sehingga proses perbaikan dapat ditelusuri kembali.