# pake def:
# lat 1:
# kalkulator (+, -, /, *)
# inputan:
# inputan angka 1 : 8
# inputan angka 2 : 10
# masukkan operator: + 
# output: hasil penjumlahan 8 + 10 = 18 

def kalkulator():
    loop = True
    while loop:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            operator = input("Masukkan operator: ")
            ops = '+-/*'
            if operator in ops:
                hasil = 0
                if operator == '+':
                    hasil = round(angka1 + angka2, 2)
                elif operator == '-':
                    hasil = round(angka1 - angka2, 2)
                elif operator == '/':
                    if angka2 == 0:
                        print('Division by zero is undefined.')
                        loop2 = True
                        while loop2:
                            lanjut = input("Ingin menggunakan kalkulator kembali? (Y/N): ").lower()
                            if lanjut == 'n':
                                print('Terima kasih.')
                                loop2 = False
                                loop = False
                            elif lanjut == 'y':
                                loop2 = False
                            else:
                                print('Hanya bisa pilih Y atau N')
                                loop2 = True
                    else:
                        hasil = round(angka1/angka2, 0)
                elif operator == '*':
                    hasil = round(angka1 * angka2, 2)
                print(f"{angka1} {operator} {angka2} = {hasil}\n")
                loop2 = True
                while loop2:
                    lanjut = input("Ingin menggunakan kalkulator kembali? (Y/N): ").lower()
                    if lanjut == 'n':
                        print('Terima kasih.')
                        loop2 = False
                        loop = False
                    elif lanjut == 'y':
                        loop2 = False
                    else:
                        print('Hanya bisa pilih Y atau N.')
                        loop2 = True
            else:
                print("Operator yang Anda masukkan salah. Masukkan operator -> +, -, *, /.")
                loop2 = True
                while loop2:
                    lanjut = input("Ingin menggunakan kalkulator kembali? (Y/N): ").lower()
                    if lanjut == 'n':
                        print('Terima kasih.')
                        loop2 = False
                        loop = False
                    elif lanjut == 'y':
                        loop2 = False
                    else:
                        print('Hanya bisa pilih Y atau N')
                        loop2 = True
        except:
            print("Input yang Anda masukkan salah.")

# kalkulator()

## 8 + 10, 8.5 + 10.5
## 8 - 19=0, 8.5 + 10
## 8 / 10, 8.5 / 10.5
## 8.5 * 10.5
## 8 'a' 10
## 8 / 0
## 'a' + 8
## 8 + 'b'

# lat 2:
# pake dict dan def:
# kamus = IND - ENG untuk hari 
# Translator (Encoder-Decoder Kode Morse)
# Silakan masukkan kalimat: Anda 
# Outputnya : (kode morse nya) * - / - - / * - / - *
# Silakan masukkan kalimat : . - / - - / . - / - .
# Outputnya : Aman
# kode morse dictionary: wikipedia

def kodemorse():
    morse = {
        'A':'.-', 
        'B':'-...', 
        'C':'-.-.', 
        'D':'-..', 
        'E':'.', 
        'F':'..-.', 
        'G':'--.', 
        'H':'....', 
        'I':'..', 
        'J':'.---', 
        'K':'-.-', 
        'L':'.-..', 
        'M':'--', 
        'N':'-.', 
        'O':'---', 
        'P':'.--.', 
        'Q':'--.-', 
        'R':'.-.', 
        'S':'...', 
        'T':'-', 
        'U':'..-', 
        'V':'...-', 
        'W':'.--', 
        'X':'-..-', 
        'Y':'-.--', 
        'Z':'--..', 
        '1':'.----', 
        '2':'..---', 
        '3':'...--', 
        '4':'....-', 
        '5':'.....', 
        '6':'-....', 
        '7':'--...', 
        '8':'---..', 
        '9':'----.', 
        '0':'-----', 
        ',':'--..--',
        '.':'.-.-.-', 
        '?':'..--..', 
        '/':'-..-.', 
        '-':'-....-', 
        '(':'-.--.', 
        ')':'-.--.-',
        ' ': ''
    }
    greet = "Translator (Encoder - Decoder Kode Morse)"
    
    loop = True
    while loop: 
        try: 
            # -.-. / .. / - / .-. / .- /  / -.. / .. / .- / -. / ..
            print("=" * len(greet))
            print(greet)
            print("=" * len(greet))
            print('Menu')
            print('1. Ubah kalimat ke kode morse.')
            print('2. Ubah kode morse ke kalimat.')
            print('3. Keluar')
            pilihan = input('Pilihan: ')
            hurufsandi = [i.lower() for i in morse.keys()]
            if pilihan == '1':
                kalimat = input("\nSilahkan masukkan kalimat Anda: ")
                hasil = ''
                for i in kalimat:
                    if i in hurufsandi:
                        hasil += morse[i.upper()] + '/'
                    else:
                        hasil = '0'
                        print('Huruf yang diinput tidak valid.')
                if hasil != '0':
                    print(f'Sandi morse dari kalimat {kalimat} adalah ')
                    print(hasil[:-1])
                loop2 = True
                while loop2:
                    pilih = input('Ingin melanjutkan Translator kembali? (Y/N): ').lower()
                    if pilih == 'n':
                        print('Terima kasih.')
                        loop2 = False
                        loop = False
                    elif pilih == 'y':
                        loop2 = False
                    elif pilih != 'y':
                        print('Hanya bisa pilih Y atau N.')
                        loop2 = True
            elif pilihan == '2':
                input_morse = input('Silakan masukkan sandi morse Anda dipisah dengan tanda baca "/" per kata: ')
                input_morse_lst = input_morse.split('/')
                switch_morse = {y:x for x, y in morse.items()}
                switch_morse_keys = list(switch_morse.keys())
                hasil = ''
                for i in input_morse_lst:
                    if i in switch_morse_keys:
                        hasil += switch_morse[i]
                    else:
                        hasil = '0'
                        print('Input yang Anda masukkan salah')
                if hasil != '0':
                    print(hasil.capitalize())
                loop2 = True
                while loop2:
                    pilih = input('Ingin melanjutkan Translator kembali? (Y/N): ').lower()
                    if pilih == 'n':
                        print('Terima kasih.')
                        loop2 = False
                        loop = False
                    elif pilih == 'y':
                        loop2 = False
                    else:
                        print('Hanya bisa pilih Y atau N.')
            elif pilihan == '3':
                print('Anda keluar dari program.')
                print('Terima kasih.')
                loop = False
            else:
                print('\nInput yang dimasukkan hanya bisa 1, 2, atau 3.\n')
        except:
            print("Input yang Anda masukkan salah.")

# Jalankan kodemorse()   
# kodemorse()

def kodemorse2():
    morse = {
        'A':'.-', 
        'B':'-...', 
        'C':'-.-.', 
        'D':'-..', 
        'E':'.', 
        'F':'..-.', 
        'G':'--.', 
        'H':'....', 
        'I':'..', 
        'J':'.---', 
        'K':'-.-', 
        'L':'.-..', 
        'M':'--', 
        'N':'-.', 
        'O':'---', 
        'P':'.--.', 
        'Q':'--.-', 
        'R':'.-.', 
        'S':'...', 
        'T':'-', 
        'U':'..-', 
        'V':'...-', 
        'W':'.--', 
        'X':'-..-', 
        'Y':'-.--', 
        'Z':'--..', 
        '1':'.----', 
        '2':'..---', 
        '3':'...--', 
        '4':'....-', 
        '5':'.....', 
        '6':'-....', 
        '7':'--...', 
        '8':'---..', 
        '9':'----.', 
        '0':'-----', 
        ',':'--..--',
        '.':'.-.-.-', 
        '?':'..--..', 
        '/':'-..-.', 
        '-':'-....-', 
        '(':'-.--.', 
        ')':'-.--.-',
        ' ': ''
    }
    greet = "Translator (Encoder - Decoder Kode Morse)"
    
    loop = True
    while loop: 
        try: 
            # -.-. / .. / - / .-. / .- /  / -.. / .. / .- / -. / ..
            print("=" * len(greet))
            print(greet)
            print("=" * len(greet))
            kalimat = input('Masukkan kalimat atau sandi morse: ').upper()
            kodemorse = morse.values()
            kodemorse_keys = morse.keys()
            switch_morse = {y:x for x, y in morse.items()}
            kalimat_morse = kalimat.replace(" ", "").split('/')
            total1 = 0
            for kode in kalimat_morse:
                # print("Kode", kode)
                for j in kodemorse:
                    if kode == j:
                        total1 += 1
            if total1 != len(kalimat_morse):
                lst = ''.join(kalimat)
                hasil = ''
                for i in lst:
                    if i in kodemorse_keys:
                        print('i', i)
                        hasil += morse[i] + '/'
                    else:
                        hasil = '0'
            elif total1 == len(kalimat_morse):
                hasil = ''
                for i in kalimat_morse:
                    hasil += switch_morse[i]
            else:
                hasil = '0'
            if hasil == '0' or '0' in hasil:
                print('Input yang Anda masukkan salah.')
                loop2 = True
                while loop2:
                    pilih = input('Ingin melanjutkan Translator kembali? (Y/N): ').lower()
                    if pilih == 'n':
                        print('Terima kasih.')
                        loop2 = False
                        loop = False
                    elif pilih == 'y':
                        loop2 = False
                    else:
                        print('Hanya bisa pilih Y atau N.')
            else:
                if total1 != '0':
                    if '/' in hasil:
                        print(f'Kode Morse dari kalimat/kata {kalimat} adalah ')
                        print(hasil)
                    else:
                        print(f'Kalimat dari kode morse {kalimat} adalah ')
                        print(hasil)
                    loop2 = True
                    while loop2:
                        pilih = input('Ingin melanjutkan Translator kembali? (Y/N): ').lower()
                        if pilih == 'n':
                            print('Terima kasih.')
                            loop2 = False
                            loop = False
                        elif pilih == 'y':
                            loop2 = False
                        else:
                            print('Hanya bisa pilih Y atau N.')
                else:
                    print('Input yang Anda masukkan salah.')
                    loop2 = True
                    while loop2:
                        pilih = input('Ingin melanjutkan Translator kembali? (Y/N): ').lower()
                        if pilih == 'n':
                            print('Terima kasih.')
                            loop2 = False
                            loop = False
                        elif pilih == 'y':
                            loop2 = False
                        else:
                            print('Hanya bisa pilih Y atau N.')
        except:
            print('Input yang Anda masukkan salah.')

# kodemorse2()


# Lat 3:
# Fizz Buzz 
# input masukkan angka :
# outputnya 
# angka yang habis bisa dibagi 3 : Fizz
# angka yang habis bisa dibagi 5 : Buzz 
# angka yang habis dibagi 3 dan dibagi 5 : Fizz Buzz 
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11

def fizzbuzz():
    loop = True
    while loop:
        try:
            angka = int(input("Masukkan angka : "))
            for i in range(1, angka + 1):
                if i % 3 == 0 and i % 5 == 0:
                    print("Fizz Buzz")
                elif  i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
            lanjut = input("Ingin melanjutkan Fizz Buzz (Y/Else)? ").lower()
            if lanjut != 'y':
                print("Thank you.")
                loop = False
        except:
            print("Angka yang Anda masukkan salah.")

# Jalankan fizzbuzz()
# fizzbuzz()

# Lat 4:
# pake def:
# Caesar cipher: 
# masukkan kata: Joni 
# masukkan angka : 2
# hasil caesar cipher : lnpk
# masukkan kata : Joni 
# masukkan angka : -2
# hasil caesar cipher: imlg
def caesar_chiper():
    loop = True 
    while loop:
        try:
            kata = input("Masukkan kata: ").lower()
            angka = int(input("Masukkan angka: "))
            alfabet = 'abcdefghijklmnopqrstuvwxyz'
            hasil = ''
            for i in kata:
                if i in alfabet:
                    idx = alfabet.index(i)
                    if (abs(angka) + idx) < len(alfabet):
                        hasil += alfabet[angka + idx]
                    else:
                        hasil += alfabet[(round(angka % len(alfabet)) + idx) % len(alfabet)]
            if len(hasil) == len(kata):   
                print(f"Kata berjumlah {angka} dari {kata} adalah {hasil}.")
            else:
                print("Input yang Anda masukkan salah.")
            lanjut = input("Ingin melanjutkan Caesar Chiper (Y/Else)? ").lower()
            if lanjut != 'y':
                print("Thank you.")
                loop = False
        except:
            print("Input Angka yang Anda masukkan salah.")
            loop = False

# Jalankan caesar_chiper
# caesar_chiper()

# Lat 5
# pake def dan dictionary
# Batasin maksimal 4000
# keluar notif : angka diluar jangkauan
# Translator (Encoder-Decoder Angka Romawi)
# silakan masukkan angka: 2018
# outputnya: (angka romawinya) MMXVIII
# silakan masukkan kalimat: MMXVIII
# output: 2018
# CCLXXVIII: 278
# MMMCMXCII.

def romawi():
    rom = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500, 
        'CM': 900,
        'M': 1000
    }

    loop = True 
    while loop:

        greet = "Translator (Encoder - Decoder Angka Romawi)"
        print(len(greet) * "=")
        print(greet)
        print(len(greet) * "=")

        angka = input("Masukkan Angka Romawi/Angka Desimal: ")
        rom_key = rom.keys()
        rom_val = rom.values()

        # Mengubah angka desimal ke angka romawi
        if angka.isdigit():
            angka = int(angka)
            if 0 < angka <= 4000:
                new_rom = {v: k for k, v in rom.items()}
                romawi_baru = ''
                sisa = int(angka)
                for i in sorted(rom_val, reverse=True):
                    if sisa >= i:
                        sisa_bagi = sisa // i
                        sisa -= (sisa_bagi * i)
                        romawi_baru += sisa_bagi * new_rom[i]
                print(f"Angka Romawi dari nilai {angka} adalah {romawi_baru}.")
                lanjut = input("Ingin melanjutkan Romawi Translator (Y/Else)? ").lower()
                if lanjut != 'y':
                    print("Thank you.")
                    loop = False
            else:
                print("Nilai hanya boleh dari rentang 1 - 4000.")
        else:
        # Mengubah angka romawi ke angka desimal
            try:
                angkasplit = list(angka)
                for i in angkasplit:
                    if i not in rom_key:
                        raise Exception("Input yang Anda masukkan salah. raise")

                duadigit = []
                idxduadigit = []
                new_list = []

                # mencari dua digit bil. Romawi dan index bil. Romawi
                for i in range(0, len(angkasplit) - 1):
                    kata = angkasplit[i] + angkasplit[i + 1]
                    # print("kata", kata)
                    if kata in rom_key:
                        duadigit.append(kata) # dua digit
                        new_list.append(kata) 
                        idxduadigit.append(i) # index dua digit ke 1
                        idxduadigit.append(i + 1) # index dua digit ke 2
                    else:
                        new_list.append(angkasplit[i])
                        break
                # print("idxduadigit", idxduadigit)
                # print("duadigit", duadigit)

                # mencari yang bukan 2 digit
                templist = []
                idxtemplist = []
                for i in range(len(angkasplit)):
                    if i not in idxduadigit:
                        templist.append(angkasplit[i])
                        idxtemplist.append(i)
                # print("templist", templist)
                # print("idxtemplist", idxtemplist)

                # mencari total dari 1 digit dan 2 digit
                total = 0
                #satu digit
                for t in templist:
                    total += rom[t]
                # dua digit
                for idx in duadigit:
                    total += rom[idx]
                
                # print("new_list", new_list)
                    
                salah = 0
                for i in range(len(new_list) - 1):
                    if rom[i] < rom[i + 1]:
                        salah += 1
                        # print("\tAngka yang Anda masukkan salah.")
                        # break
                if salah == 0:
                    print(f"Angka Desimal dari Angka Romawi {angka} adalah {total}.")
                else:
                    print("\tAngka yang Anda masukkan salah.")
                        # break

                lanjut = input("Ingin melanjutkan Romawi Translator (Y/Else)? ").lower()
                if lanjut != 'y':
                    print("Thank you.")
                    loop = False
            except:
                print("Input yang Anda masukkan salah.")
         
# Jalankan Fungsi romawi()
# romawi()


# Lat 6
# konversi angka digital
# masukkan angka: 9
# output:
#  __
# |__|
#  __|

def konversi_angka():
    loop = True
    while loop:
        try:
            angka = input("Masukkan angka 0 - 9: ")
            z = ''
            if angka == '0':
                z += ' ___ \n'
                z += '|   |\n'
                z += '|   |\n'
                z += '|___|\n'
            elif angka == '1':
                z += '  |  \n'
                z += '  |  \n'
                z += '  |  \n'
            elif  angka == '2':
                z += ' __ \n'
                z += ' __|\n'
                z += '|__ \n'
            elif angka == '3':
                z += ' __ \n'
                z += ' __|\n'
                z += ' __|\n'
            elif angka == '4':
                z += '    \n'
                z += '|__|\n'
                z += '   |\n'  
            elif angka == '5':
                z += ' __ \n'
                z += '|__\n'
                z += ' __|\n' 
            elif angka == '6':
                z += ' __ \n'
                z += '|__ \n'
                z += '|__|\n'    
            elif angka == '7':
                z += ' __ \n'
                z += '   |\n'
                z += '   |\n'  
            elif angka == '8':
                z += ' __ \n'
                z += '|__|\n'
                z += '|__|\n' 
            elif angka == '9':
                z += ' __ \n'
                z += '|__|\n'
                z += ' __|\n' 
            else:
                print('Angka yang Anda masukkan salah.')
            if z != '':
                print(z)
            lanjut = input("Ingin melanjutkan Konversi Angka (Y/Else)? ").lower()
            if lanjut != 'y':
                print("Thank you.")
                loop = False
        except:
            print("Angka yang Anda masukkan salah.")

# konversi_angka()

# Rekursif
# 2! = 2 x 1
# 3! = 3 x 2 x 1
# 5! = 5 x 4 x 3 x 2 x 1

def faktorial(x):
    if (x <= 2):
        return x
    else:
        return x * faktorial(x - 1)

# print(faktorial(2))
# print(faktorial(3))
# print(faktorial(4))
