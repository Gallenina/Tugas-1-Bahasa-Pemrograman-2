# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(jari_jari):
    pi = 3.14  # Nilai pi
    return pi * jari_jari**2

# Input dari pengguna
jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))

# Menghitung dan menampilkan luas
luas = hitung_luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")
