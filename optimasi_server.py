
# Program Optimasi Biaya Sewa Cloud Server
# Mata Kuliah: Pemodelan dan Simulasi

# Tarif sewa server per jam
biaya_standar = 8000
biaya_performa = 12000

# Kapasitas Server Standar per jam
instruksi_standar = 20
database_standar = 10

# Kapasitas Server Performa Tinggi per jam
instruksi_performa = 10
database_performa = 30

# Kebutuhan minimum
kebutuhan_instruksi = 100
kebutuhan_database = 90

# Model matematika:
# 20x + 10y = 100
# 10x + 30y = 90
#
# Disederhanakan menjadi:
# 2x + y = 10
# x + 3y = 9

# Menghitung titik potong kedua persamaan
x = 21 / 5
y = 10 - (2 * x)

# Menghitung hasil pemrosesan
total_instruksi = (
    instruksi_standar * x
    + instruksi_performa * y
)

total_database = (
    database_standar * x
    + database_performa * y
)

# Menghitung biaya sewa
total_biaya = (
    biaya_standar * x
    + biaya_performa * y
)

# Menampilkan hasil
print("=" * 45)
print("OPTIMASI BIAYA SEWA CLOUD SERVER")
print("=" * 45)

print(f"Durasi Server Standar        : {x:.1f} jam")
print(f"Durasi Server Performa Tinggi: {y:.1f} jam")

print("-" * 45)
print(f"Total instruksi pemrosesan   : {total_instruksi:.0f}")
print(f"Total akses basis data       : {total_database:.0f}")
print(f"Total biaya sewa             : Rp{total_biaya:,.0f}")

# Memeriksa apakah kebutuhan telah terpenuhi
print("-" * 45)

if (
    total_instruksi >= kebutuhan_instruksi
    and total_database >= kebutuhan_database
):
    print("Status: Semua kebutuhan terpenuhi.")
else:
    print("Status: Kebutuhan belum terpenuhi.")

print("=" * 45)
