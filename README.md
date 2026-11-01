# Pertemuan 13 - Debugging dan Testing

**Nama:** Putri Ayu Anisa Mahie  
**NIM:** 2225250167  
**Kelas:** 3F

## Kasus

Program yang diuji adalah program analisis nilai mahasiswa menggunakan Python. Program memiliki tiga fungsi, yaitu `hitung_rata_rata()` untuk menghitung rata-rata nilai, `status()` untuk menentukan kelulusan, dan `nilai_tertinggi()` untuk mencari nilai terbesar.

Pengujian dilakukan untuk menemukan kesalahan pada indentasi, perhitungan rata-rata, dan logika pencarian nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC01 | `[80, 60, 90, 70]` | Rata-rata: 75.0 | Rata-rata: 60.0 | Gagal |
| TC02 | `status(60)` | Tidak lulus | Tidak lulus | Lulus |
| TC03 | `[80, 60, 90, 70]` | Nilai tertinggi: 90 | Nilai tertinggi: 0 | Gagal |

## Bug Report

**1. Bug pada perhitungan rata-rata**
- **Gejala:** Hasil rata-rata tidak sesuai.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Program membagi jumlah nilai dengan angka tetap `5`, padahal terdapat 4 data.
- **Perbaikan:** Mengganti `sum(nilai) / 5` menjadi `sum(nilai) / len(nilai)`.

**2. Bug pada pencarian nilai tertinggi**
- **Gejala:** Program menghasilkan nilai tertinggi yang salah.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Kondisi perbandingan menggunakan `x < tertinggi`, sehingga logikanya terbalik.
- **Perbaikan:** Menggunakan `x > tertinggi` dan menginisialisasi `tertinggi` dengan `nilai[0]`.

**3. Bug pada indentasi**
- **Gejala:** Program mengalami `IndentationError`.
- **Lokasi:** Bagian isi fungsi dan percabangan.
- **Akar penyebab:** Baris kode tidak menggunakan indentasi yang benar.
- **Perbaikan:** Menambahkan indentasi empat spasi pada blok fungsi, perulangan, dan percabangan.

## Retest

Setelah perbaikan, program dijalankan kembali dengan input `[80, 60, 90, 70]`.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| TC01 | Rata-rata: 75.0 | Rata-rata: 75.0 | Lulus |
| TC02 | Tidak lulus | Tidak lulus | Lulus |
| TC03 | Nilai tertinggi: 90 | Nilai tertinggi: 90 | Lulus |

## Cara Menjalankan

Jalankan perintah berikut pada terminal VS Code dari folder utama proyek:

```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah memeriksa nilai variabel, kondisi percabangan, dan hasil keluaran program. Teknik ini membantu menemukan penyebab kesalahan sehingga kode dapat diperbaiki dan diuji kembali untuk memastikan hasilnya benar.