# tugas/tabel_perkalian_dan_statistik.py

print("Tabel Perkalian dan Statistik")

# 1. Baca dan validasi n (n harus > 0)
n = int(input("n: "))
while n <= 0:
    n = int(input("n harus > 0. Masukkan n kembali: "))

# 2. Inisialisasi total keseluruhan dan pencacah bilangan genap
total_semua = 0
count_genap = 0

print("\nTabel Perkalian:")

# 3. Nested loop untuk membentuk tabel n x n
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        total_baris += hasil
        total_semua += hasil
        
        # Cek apakah hasil genap
        if hasil % 2 == 0:
            count_genap += 1
            
        # Tampilkan hasil perkalian secara rata kanan (lebar kolom 4 karakter)
        print(f"{hasil:4d}", end="")
    
    # Tampilkan total per baris di akhir setiap baris
    print(f" | Total baris {i} = {total_baris}")

# 4. Tampilkan statistik keseluruhan
print("-" * 35)
print(f"Total semua          = {total_semua}")
print(f"Banyak hasil genap  = {count_genap}")