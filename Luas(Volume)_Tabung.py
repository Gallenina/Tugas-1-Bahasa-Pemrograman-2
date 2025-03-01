# Fungsi untuk menghitung volume tabung
def hitung_volume_tabung(jari_jari, tinggi):
    pi = 3.14  # Nilai pi
    return pi * jari_jari**2 * tinggi

# Input dari pengguna
jari_jari = float(input("Masukkan panjang jari-jari alas tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

# Menghitung dan menampilkan volume
volume = hitung_volume_tabung(jari_jari, tinggi)
print(f"Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah {volume}")
