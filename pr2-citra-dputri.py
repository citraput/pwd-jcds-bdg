#############################################################
# Soal 1
#############################################################
# Input: Masukkan nilai
# Kondisi:
# nilai diatas 100: Nilai diluar jangkauan
# nilai dibawah 0: Tidak bisa menerima nilai negatif
# diatas 90: grade A 
# diatas 85: grade A-
# diatas 80: grade B
# diatas 75: grade B-
# diatas 70: grade C
# diatas 65: grade D
# di bawah itu remedial

nilai = int(input("Masukkan nilai Anda: "))
if nilai > 100:
    print("Nilai diluar jangkauan.")
elif nilai < 0:
    print("Tidak bisa menerima nilai negatif.")
elif nilai > 90:
    print("Nilai Anda: {} dan Grade Anda: A.".format(nilai))
elif nilai > 85:
    print("Nilai Anda: {} dan Grade Anda: A-.".format(nilai))
elif nilai > 80:
    print("Nilai Anda: {} dan Grade Anda: B.".format(nilai))
elif nilai > 75:
    print("Nilai Anda: {} dan Grade Anda: B-.".format(nilai))
elif nilai > 70:
    print("Nilai Anda: {} dan Grade Anda: C.".format(nilai))
elif nilai > 65:
    print("Nilai Anda: {} dan Grade Anda: D.".format(nilai))
else:
    print("Anda harus remedial.")
print()
#############################################################
# Soal 2
#############################################################
# input: masukkan angka
# kondisi: cek angka
# output: angka yang Anda masukkan adalah (angka) adalah angka GENAP/GANJIL

angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print("Angka yang Anda masukkan {} adalah angka genap.".format(angka))
else:
    print("Angka yang Anda masukkan {} adalah angka ganjil.".format(angka))
print()

#############################################################
# Soal 3
#############################################################
# rumus : IMT = massa (kg) / tinggi (m) ^ 2

# input : 
# masukkan Massa (Kg)
# masukkan tinggi (cm)

# Kondisi :
#  IMT < 18.5 = berat badan kurang
#  18.5 - 24.9 = berat badan ideal
#  25 - 29.9 = berat badan berlebih
#  30 - 39.9 = BB sangat berlebih 
#  IMT > 39.9 = obesitas

#  Output :
#  Massa : (massa) (Kg)
# Tinggi : (tinggi) (m) 
# IMT ....., BERAT BADAN ANDA IDEAL (sesuai kondisi)

massa = int(input("Masukkan Massa (kg) : "))
tinggi = int(input("Masukkan Tinggi (cm) : "))

imt = massa / ((tinggi / 100) ** 2)
if (imt < 18.5):
    ket = "Berat badan kurang"
elif (imt >= 18.5 and imt <= 24.9):
    ket = "Berat badan Anda ideal"
elif (imt >= 25.0 and imt <= 29.9):
    ket = "Berat badan Anda berlebih"
elif (imt >= 30.0 and imt <= 39.9):
    ket = "Berat badan Anda sangat berlebih"
else:
    ket = "Obesitas"
print(f"Massa {massa} kg dan tinggi {tinggi/100} m\nIMT = {round(imt, 2)}, {ket}.")

