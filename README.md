# Pertemuan 06 Nested Loop Python

**Algoritma dan Pemrograman | Pertemuan 06**

**Nama:** Fridha Septiana
**NIM:** 2225250068
**Kelas:** 3E

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan untuk menyelesaikan permasalahan menggunakan Python.

## Cara Menjalankan

Program dapat dijalankan melalui terminal dengan perintah:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

Pada Windows, dapat juga menggunakan:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

1. Program menampilkan judul **Tabel Perkalian dan Statistik**.
2. Program membaca bilangan bulat `n`.
3. Jika `n <= 0`, program meminta input `n` kembali sampai mendapatkan bilangan positif.
4. Menginisialisasi `total_semua = 0` sebagai akumulator untuk menjumlahkan seluruh hasil perkalian.
5. Menginisialisasi `count_genap = 0` sebagai counter untuk menghitung banyak hasil perkalian yang genap.
6. **Loop luar** menggunakan `i` dari 1 sampai `n` untuk mengatur setiap baris tabel.
7. Pada setiap baris, `total_baris` diatur kembali menjadi 0.
8. **Loop dalam** menggunakan `j` dari 1 sampai `n` untuk mengatur setiap kolom.
9. Menghitung `hasil = i * j`.
10. Menambahkan `hasil` ke `total_baris` dan `total_semua`.
11. Jika `hasil` genap, `count_genap` ditambah 1.
12. Setelah loop dalam selesai, program menampilkan jumlah setiap baris.
13. Setelah nested loop selesai, program menampilkan total keseluruhan dan banyak hasil yang genap.

**Peran masing-masing bagian:**

* **Loop luar:** mengatur baris tabel perkalian.
* **Loop dalam:** mengatur kolom dan menghitung setiap pasangan `i` dan `j`.
* **Akumulator:** `total_baris` dan `total_semua` digunakan untuk menjumlahkan hasil perkalian.
* **Counter:** `count_genap` digunakan untuk menghitung banyak hasil perkalian yang genap.

## Hasil Pengujian

| Input   | Hasil yang Diharapkan       | Keluaran Aktual             | Status   |
| ------- | --------------------------- | --------------------------- | -------- |
| `n = 1` | Total = 1, hasil genap = 0  | Total = 1, hasil genap = 0  | Berhasil |
| `n = 2` | Total = 9, hasil genap = 3  | Total = 9, hasil genap = 3  | Berhasil |
| `n = 3` | Total = 36, hasil genap = 5 | Total = 36, hasil genap = 5 | Berhasil |

### Detail Jumlah Setiap Baris

| Input   | Jumlah Setiap Baris | Total Keseluruhan | Hasil Genap |
| ------- | ------------------- | ----------------: | ----------: |
| `n = 1` | 1                   |                 1 |           0 |
| `n = 2` | 3, 6                |                 9 |           3 |
| `n = 3` | 6, 12, 18           |                36 |           5 |

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali. Pada setiap perulangan loop luar, loop dalam juga berjalan sebanyak `n` kali.

Jadi, badan loop dalam berjalan sebanyak:

**n × n = n² kali**

Dengan demikian, kompleksitas waktu program adalah **O(n²)**.

Contohnya, jika `n = 3`, badan loop dalam berjalan:

**3 × 3 = 9 kali**

Jika `n = 5`, badan loop dalam berjalan:

**5 × 5 = 25 kali**

## Refleksi

Kesalahan yang dapat terjadi pada nested loop adalah kesalahan indentasi, misalnya menempatkan `total_baris = 0` di luar loop `i`. Jika hal tersebut terjadi, jumlah setiap baris akan terus terakumulasi dan hasilnya menjadi tidak sesuai.

Cara memperbaikinya adalah memastikan `total_baris = 0` berada di dalam loop luar sehingga setiap baris memulai perhitungan dari 0. Selain itu, loop dalam harus berada di dalam loop luar dengan indentasi yang benar.
