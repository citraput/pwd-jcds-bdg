##################################################################################
# Soal 1
##################################################################################
hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
# print(*hari, sep='\n')
# senin --> 2 hari : rabu
# input: masukkan nama hari: SENIN atau selasA 
# jumlah: 100 hari 
# output: <hari> hari dari sekarang <nama hari> adalah hari .... 
# kondisi pengecekan input: "Tidak ada nama hari"

# Membuat input menjadi lowercase seperti variabel hari
input_hari = input("Masukkan nama hari: ").lower()
# Kondisi hari Jum'at
try: 
    if input_hari == 'jumat':
        input_hari = "jum'at"
    # Jika input_hari ada di dalam variabel hari
    if input_hari in hari:
        jumlah = int(input("Masukkan jumlah hari: "))
        if (abs(jumlah) + hari.index(input_hari)) < len(hari):
            print(str(jumlah) + " hari dari sekarang " + input_hari.capitalize(),(hari[jumlah + hari.index(input_hari)]).capitalize())
        else:
            print(str(jumlah) + " hari dari sekarang " + input_hari.capitalize(), (hari[(round(jumlah % len(hari)) + hari.index(input_hari)) % len(hari)]).capitalize())
# Jika input_hari tidak ada di dalam variabel hari
except:
    print("Tidak ada nama hari.")

# kalimat = kalimat[:] # jadi 2 variabel yang berbeda

###################################################################################
# Soal 2
###################################################################################
# palindrome
kata = input("Masukkan kata: ")
# Membuat kata lowercase
if kata.lower() == kata[::-1].lower():
    print("Kata tersebut termasuk palindrome.")
else:
    print("Kata tersebut bukan palindrome.")

###################################################################################
# Soal 3
###################################################################################
# masukkan kalimat: "hari ini hari selasa"
# 1. masukkan karakter: "a"
# output: hri ini hri sels
# 2. masukkan karakter vokal: "o"
# output: horo ono horo soloso

kalimat = input("Masukkan kalimat: ")
karakter = input("Masukkan karakter: ")
# Opsi 1
print(kalimat.replace(karakter,""))
# Opsi 2
vokal_input = input("Masukkan karakter vokal: ") #'a', 'i', 'u', 'e', 'o'
vokal = 'aiueo'
for huruf in kalimat: # h, a, r, i, ,i, n, i, , h, a, r, i, , s, e, l, a, s, a
    if huruf in vokal: # if h in 'aiueo'
        kalimat = kalimat.replace(huruf, vokal_input)
    # print(i)
print(kalimat)

# # try-catch

###################################################################################
# Soal 4 
###################################################################################
# try-except
# (hanya menggunakan metode numerikal)
# masukan 4 digit angka: 5689
# outputnya 8956
try:
    num = input("Masukkan 4 digit angka: ")
    # Memastikan angka yang dimasukkan 4 digit
    if len(num) == 4:
        num = int(num)
        angka1 = (num - (num//100 * 100)) * 100
        angka2 = num // 100
        print(angka1 + angka2)
    else:
        # Jika angka bukan 4 digit
        print("Angka yang Anda masukkan salah.")
except:
    # Jika yang dimasukkan bukan angka
    print("Angka yang Anda masukkan salah.")

###################################################################################
# Soal 5
# ################################################################################### 
# try-except
# input masukkan angka 2 digit: 85 
# masukkan 2 digit kedua: 32 
# output: 8532
try:
    angka1 = int(input("Masukkan angka pertama 2 digit: "))
    angka2 = int(input("Masukkan angka kedua 2 digit: "))
    # mengecek kedua angka 2 digit
    # == in not !=
    # not in (membership) --> !=
    # len(angka1) == 2 and len(angka2) == 2
    if 10 <= angka1 < 100 and 10 <= angka2 < 100:
        print(angka1 * 100 + angka2)
    else:
        # jika tidak 2 digit
        print("Angka yang Anda masukkan salah.")
except:
    # jika yang dimasukkan bukan angka
    print("Angka yang Anda masukkan salah.")
    
