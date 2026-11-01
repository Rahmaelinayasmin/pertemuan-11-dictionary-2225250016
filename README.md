
# PERTEMUAN 11 - DICTIONARY/MAP

## Identitas Mahasiswa

Nama  : (Rahma Elina Yasmin)
NIM   : (2225250016)
Kelas : (3F)

## Tujuan

Tujuan praktikum ini adalah menggunakan dictionary/map untuk merepresentasikan data dalam bentuk pasangan key-value.

Adapun tujuan khususnya:
1. Memahami perbedaan list dan dictionary.
2. Membuat dictionary dengan pasangan key-value.
3. Mengakses data menggunakan key.
4. Menggunakan get() untuk akses data yang aman.
5. Menambah, mengubah, dan menghapus data.
6. Menelusuri dictionary menggunakan keys(), values(), dan items().
7. Menggunakan dictionary bersarang.
8. Menggunakan fungsi untuk mengolah dictionary.
9. Memodelkan data mahasiswa menggunakan dictionary.

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama.

Setiap value berisi:
- Nama mahasiswa.
- Kelas mahasiswa.
- Nilai mahasiswa.

Contoh:

    data_mahasiswa = {
        "A001": {
            "nama": "Ayu",
            "kelas": "A",
            "nilai": 85
        }
    }

## Cara Menjalankan

1. Buka folder project melalui Visual Studio Code.
2. Pastikan Python 3 sudah terinstal.
3. Buka Terminal pada VS Code.
4. Jalankan file latihan menggunakan perintah:

    python latihan/01_dasar_dictionary.py

5. Untuk menjalankan program praktik, gunakan:

    python praktik/data_mahasiswa.py

## Tabel Pengujian

| No | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|------------|----------------------|--------------|--------|
| 1 | Mencari A003 | Data Citra ditampilkan | Data Citra ditampilkan | Berhasil |
| 2 | Mencari A999 | Data tidak ditemukan | Data tidak ditemukan | Berhasil |
| 3 | Menambahkan A006 | Data Fajar berhasil ditambahkan | Data Fajar berhasil ditambahkan | Berhasil |
| 4 | Mengubah nilai A002 menjadi 82 | Nilai berubah menjadi 82 | Nilai berubah menjadi 82 | Berhasil |
| 5 | Menampilkan items() | Seluruh data mahasiswa tampil | Seluruh data mahasiswa tampil | Berhasil |
| 6 | Menghitung rata-rata | Menghasilkan 83.50 | Menghasilkan 83.50 | Berhasil |

## Refleksi

Kesalahan yang dapat terjadi ketika menggunakan dictionary adalah KeyError, yaitu ketika program mengakses key yang tidak tersedia.

Cara memperbaikinya adalah menggunakan method get() atau memeriksa keberadaan key menggunakan operator in sebelum mengakses data.

Melalui praktikum ini, saya memahami bahwa dictionary mempermudah pencarian dan pengelolaan data karena setiap informasi dapat diakses berdasarkan key. Saya juga memahami cara menambahkan, mengubah, menghapus, dan menampilkan data mahasiswa menggunakan dictionary.

## Kesimpulan

Dictionary merupakan struktur data Python yang menyimpan pasangan key-value. Dictionary dapat digunakan untuk menyimpan, mencari, mengubah, dan menghapus data secara lebih terstruktur.

Pada praktikum ini, dictionary digunakan untuk mengelola data mahasiswa berdasarkan NIM dan menghitung rata-rata nilai mahasiswa.
