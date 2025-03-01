# Fungsi untuk menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Menghitung dan menampilkan luas
luas = hitung_luas_persegi_panjang(panjang, lebar)
print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
