
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

# Menentukan gaji dan bonus berdasarkan status dan golongan
if status == "Tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
    else:
        bonus = "Status Tidak Valid, Coba lagi."
elif status == "Honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000
    else:
        bonus = "Status Tidak Valid, Coba lagi."
else:
    print("Status tidak valid!")

exit()

# Menghitung total gaji
gaji_total = gaji + bonus

# Menampilkan hasil
print("\n=== Rincian Gaji ===")
print("Gaji Pokok: Rp" + str(format(gaji, ",")))
print("Bonus: Rp" + str(format(bonus, ",")))
print("Gaji Total: Rp" + str(format(gaji_total, ",")))
