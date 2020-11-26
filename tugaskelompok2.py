# # Team Assignment
# # Kelompok 2 - 3 orang

# Ketika di run awal:
# MENU - Login dan Register

# --> Menu Register 
# Masukkan data 
# USER ID: ... (harus kombinasi huruf dan angka) === lakukan pengecekan 
# duplikasi, tidak boleh ada user id yang sama 
# Password: ... (harus gabungan huruf kapital, huruf kecil dan angka, 
# minimal 8 karakter)
# Email: ... (lakukan verifikasi email)
# Ketentuan valid dan tidak valid sesuai tugas sebelumnya 

    # datapersonal = {
    #     'nama': '',
    #     'userid': '',
    #     'password':'',
    #     'email': '',
    #     'gender': '',
    #     'usia': 0,
    #     'pekerjaan': '',
    #     'hobi': [],
    #     'alamat': '',
    #     'namakota': '',
    #     'rt': 0,
    #     'rw': 0,
    #     'zipcode': 0,
    #     'geo': {
    #         'lat': 0,
    #         'long': 0
    #     },
    #     'nohp': ''
    # }
# Nama : ... 
# Gender: .... 
# usia: .... 
# pekerjaan: ... 
# hobi: (isi lebih dari satu)
# alamat:  
# Nama kota: 
# RT: 
# RW: 
# Zip Code: 
# Geo: Lat - Langitude 
# No HP : .... 

# Simpan (Y/N)
# -- kalau Y: data tersimpan 
# -- kalau N: data tidak tersimpan 

# Baik Y atau N ===> Kembali ke menu awal 
# Menu awal : Login atau Register 

# -- Menu Login :
# Masukkan ID dan Password == Lakukan pengecekan ID dan password 
# ## ID salah atau password salah atau ID tidak terdaftar
# # - OK ? Anda berhasil login 

# ### MENU UTAMA 
# 1. Data Personal 
# diklik: Keluar seluruh data personal 
# username dan data id tidak perlu ditampilkan 
# Nama : ... 
# Email:...
# Gender: .... 
# usia: .... 
# pekerjaan: ... 
# hobi: (isi lebih dari satu)
# alamat:  
# Nama kota: 
# RT: 
# RW: 
# Zip Code: 
# Geo: Lat - Langitude 
# No HP : .... 

# 2. Konversi Kode Morse 
# 3. Kalkulator
# 4. Konversi Romawi 
# 5. Hitung hari # masukkan hari terus angka, 100 hari dari hari ini adalah...
# 6. Kamus hari (ENG - IND & IND - ENG) # Auto Detect
# 7. Manipulasi karakter: (atau bisa kalian ganti dengan project lain)
# 8. Konversi jumlah hari (dari inputan ubah ke tahun, bulan, minggu, hari)
# 9. Nilai Faktorial 
# 10. Jumlah angka Fibonacci (sesuai inputan user input 7 deret pertama bilangan fibonacci) --> jumlah 7 deret pertama bilangan fibonacci dan keluarkan deretnya
# 11. Data USER -- menampilkan user ID dan password serta email dari seluruh data yang ada
# 12. MENU CRUD:
# opsi: Nama dan stok = toko 
# Nama barang dan harga = Toko - kasir 
# Nama karyawan dan gaji = Penggajian 
# Nama Mahasiswa dan nilai = Kampus 

# ** Optional: Boleh tambahkan fungsi lain 
# *** Coba gunakan def, lambda, filter reduce dan map 

# no 3 dan 7 bisa project lain
# *** kirim email: deadline, 31 Mei 2020

namakota = ['Banda Aceh', 'Langsa', 'Lhokseumawe', 'Meulaboh', \
    'Sabang', 'Subulussalam', 'Denpasar', 'Pangkalpinang', 'Cilegon', \
    'Serang', 'Tangerang-Selatan', 'Tangerang', 'Bengkulu', 'Gorontalo',\
    'Jakarta Barat', 'Jakarta Pusat', 'Jakarta Selatan', 'Jakarta Timur',\
    'Jakarta Utara', 'Sungai Penuh', 'Jambi', 'Bandung', 'Bekasi', 'Bogor',\
    'Cimahi', 'Cirebon', 'Depok', 'Sukabumi', 'Tasikmalaya', 'Banjar', 'Magelang',\
    'Pekalongan', 'Purwokerto', 'Salatiga', 'Semarang', 'Surakarta', 'Tegal', 'Batu',\
    'Blitar', 'Kediri', 'Madiun', 'Malang', 'Mojokerto', 'Pasuruan', 'Probolinggo',\
    'Surabaya', 'Pontianak', 'Singkawang', 'Banjarbaru', 'Banjarmasin', 'Palangkaraya',\
    'Balikpapan', 'Bontang', 'Samarinda', 'Tarakan', 'Batam', 'Tanjungpinang', 'Bandar Lampung',\
    'Metro', 'Ternate', 'Tidore', 'Ambon', 'Tual', 'Bima', 'Mataram', 'Kupang', \
    'Sorong', 'Jayapura', 'Dumai', 'Pekanbaru', 'Makassar', 'Palopo', 'Parepare',\
    'Palu', 'Bau-Bau', 'Kendari', 'Bitung', 'Kotamobagu', 'Manado', 'Tomohon',\
    'Bukittinggi', 'Padang', 'Padangpanjang', 'Pariaman', 'Payakumbuh', 'Sawahlunto',\
    'Solok', 'Lubuklinggau', 'Pagaralam', 'Palembang', 'Prabumulih', 'Binjai', 'Medan',\
    'Padang Sidempuan', 'Pematangsiantar', 'Sibolga', 'Tanjungbalai', 'Tebingtinggi', 'Yogyakarta']

def login(userid, passworduser):
    import json
    with open('Tugas_Kelompok/datausers.json', 'r') as json_file:
        data = json.load(json_file)
        # {datauser : [{nama:, passworduser}, {}, {}]}
    for user in data['datauser']:
        if (user['userid'] == userid) and (user['password'] == passworduser):
            return True
        elif (user['userid'] == userid) and not (user['password'] == passworduser):
            return 'password'
        elif not (user['userid'] == userid) and (user['password'] == passworduser):
            return 'userid'

def datauser(userid, passworduser):
    import json
    with open('Tugas_Kelompok/datausers.json') as json_file:
        data = json.load(json_file)['datauser']
        for user in data:
            if (user['userid'] == userid) and (user['password'] == passworduser):
                return user

def cekUserId(userid):
    import json
    with open('Tugas_Kelompok/datausers.json') as json_file:
        datas = json.load(json_file)['datauser']
        if len(datas) == 0:
            return False
        else:
            for data in datas:
                if data['userid'] == userid:
                    return True
                else:
                    return False
                    
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
            print()
            print("\t" + "=" * len(greet))
            print("\t" + greet)
            print("\t" + "=" * len(greet))
            loopMorse = True
            while loopMorse:
                kalimat = input("\n\tSilahkan masukkan kalimat Anda: ").lower()
                hurufsandi = [i.lower() for i in morse.keys()]
                kodemorse = morse.values()
                kalimatlen = len(kalimat)
                kalimatlensplit = len(kalimat.split('/'))

                total1 = 0
                for kode in kalimat.replace(" ", "").split('/'):
                    # print("Kode", kode)
                    for j in kodemorse:
                        if kode == j:
                            total1 += 1

                # Kondisi Titik, jumlah morse : 1 - 5
                titik = 0
                for kode in kalimat:
                    if kode == '.':
                        titik += 1
                # print(titik)

                # Kondisi "-", jumlah = 3
                strip = 0
                for kode in kalimat:
                    if kode == '-':
                        strip += 1

                # print("Kalimat len: ", kalimatlen)
                # print("Kalimat len split: ", kalimatlensplit)
                # print("Total 1: ", total1)

                if kalimatlensplit == total1 and kalimatlen != titik and kalimatlen != strip:
                    if '/' in kalimat:
                        sandi_input = kalimat.replace(" ", "").split('/')
                    else:
                        sandi_input = [kalimat]
                    sandimorse = morse.values()
                    decode = []
                    for sandi in sandi_input:
                        if sandi in sandimorse:
                            for key, val in morse.items():
                                if val == sandi:
                                    decode.append(key)
                    if len(decode) == len(sandi_input):
                        new_decode = ''
                        for i in decode:
                            new_decode += i
                        print(f"\tKalimat dari sandi morse {kalimat} adalah {new_decode.title()}\n")

                        loop3 = True
                        while loop3:
                            lanjut = input("\t\t** Ingin menggunakan translator kode morse kembali? (Y/N): ").lower()
                            # if lanjut != 'y':
                            #     print('\tThank you.\n')
                            #     loop = False
                            if lanjut == 'n':
                                print('\t\t** Keluar dari Translator Kode Morse\n')
                                loop3 = False
                                loop = False
                                loopMorse = False
                            elif lanjut != 'y':
                                print("\t\t** Input yang Anda masukkan salah. Pilih Y atau N.")
                            else:
                                loop3 = False
                    else:
                        print("\t\t** Sandi Morse yang Anda masukkan salah.")
                else:

                    encode = []
                    for huruf in kalimat:
                        if huruf in hurufsandi:
                            encode.append(morse[huruf.upper()])   
                        else:
                            print("\t\t** Kalimat yang Anda masukkan salah.")
                            break
                            # loop3 = True
                            # while loop3:
                            #     lanjut = input("\t\t** Ingin menggunakan translator kode morse kembali? (Y/N): ").lower()
                            #     if lanjut == 'n':
                            #         print('\t\t** Keluar dari translator Kode Morse\n')
                            #         loop3 = False
                            #         loopMorse = False
                            #         loop = False
                            #     elif lanjut != 'y':
                            #         print("\t\t** Input yang Anda masukkan salah. Pilih Y atau N.")
                            #     else:
                            #         loop3 = False
                            #         break

                    # print(encode)
                    if len(encode) == len(kalimat):
                        print(f"\tSandi Morse dari kalimat {kalimat} adalah {' / '.join(encode)}\n")
                        loop3 = True
                        while loop3:
                            lanjut = input("\t\t** Ingin menggunakan translator kode morse kembali? (Y/N): ").lower()
                            if lanjut == 'n':
                                print('\t\t** Keluar dari translator Kode Morse\n')
                                loop3 = False
                                loopMorse = False
                                loop = False
                            elif lanjut != 'y':
                                print("\t\t** Input yang Anda masukkan salah. Pilih Y atau N.")
                            else:
                                loop3 = False
                                # print('\tThank you.\n')
                                # loop = False
                    else:
                        loop3 = True
                        while loop3:
                            lanjut = input("\t\t** Ingin menggunakan translator kode morse kembali? (Y/N): ").lower()
                            if lanjut == 'n':
                                print('\t\t** Keluar dari translator Kode Morse\n')
                                loop3 = False
                                loopMorse = False
                                loop = False
                            elif lanjut != 'y':
                                print("\t\t** Input yang Anda masukkan salah. Pilih Y atau N.")
                            else:
                                loop3 = False
        except:
            print("\t\t** Input yang Anda masukkan salah.")
            loop = False

def kalkulator():
    print("\t" + "=" * 10)
    print("\tKALKULATOR")
    print("\t" + "=" * 10)
    loop = True
    program = 'Program Kalkulator'
    while loop:
        try:
            angka1 = float(input("\tMasukkan angka pertama: "))
            angka2 = float(input("\tMasukkan angka kedua: "))
            operator = input("\tMasukkan operator: ")
            if operator in ['+', '-', '/', '*', '%']:
                hasil = 0
                if operator == '+':
                    hasil = round(angka1 + angka2, 2)
                elif operator == '-':
                    hasil = round(angka1 - angka2, 2)
                elif operator == '/':
                    if angka2 == 0:
                        print("\tDivision by zero is undefined.")
                    else:
                        hasil = round(angka1 / angka2, 2)
                elif operator == '*':
                    hasil = round(angka1 * angka2, 2)
                elif operator == '%':
                    hasil = round(angka1 % angka2, 2)
                
                if int(angka2) != 0 and operator != '/':
                    print(f"\t>> {angka1} {operator} {angka2} = {hasil}\n")
                    loop = lanjut2(program)
                else:
                    loop = lanjut2(program)
            else:
                print("\t\t** Operator yang diinput harus +, -, /, *, atau %")
                loop = lanjut2(program)
        except:
            print("\t\t** Input yang Anda masukkan salah.")
            loop = lanjut2(program)

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

    program = "Program Translator (Encoder - Decoder Angka Romawi)"
    greet = "\t\t\tTranslator (Encoder - Decoder Angka Romawi)"
    print("\t" + (len(greet) + 43) * "=")
    print(greet)
    print("\t" + (len(greet) + 43) * "=")

    loop = True 
    while loop:

        angka = input("\n\tMasukkan Angka Romawi/Angka Desimal: ")
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
                print(f"\tAngka Romawi dari nilai {angka} adalah {romawi_baru}.\n")
                # loop = lanjut2(program)
            else:
                print("\t\t** Nilai hanya boleh dari rentang 1 - 4000.")
                # loop = lanjut2(program)
            loop = lanjut2(program)
        else:
        # Mengubah angka romawi ke angka desimal
            try:
                angkasplit = list(angka)
                for i in angkasplit:
                    if i not in rom_key:
                        raise Exception("\t\t** Input yang Anda masukkan salah. raise")

                duadigit = []
                idxduadigit = []

                # mencari dua digit bil. Romawi dan index bil. Romawi
                for i in range(0, len(angkasplit) - 1):
                    kata = angkasplit[i] + angkasplit[i + 1]
                    if kata in rom_key:
                        duadigit.append(kata) # dua digit
                        idxduadigit.append(i) # index dua digit ke 1
                        idxduadigit.append(i + 1) # index dua digit ke 2
                # print(idxduadigit)

                # mencari yang bukan 2 digit
                templist = []
                for i in range(len(angkasplit)):
                    if i not in idxduadigit:
                        templist.append(angkasplit[i])
                
                # mencari total dari 1 digit dan 2 digit
                total = 0
                #satu digit
                for t in templist:
                    total += rom[t]
                # dua digit
                for idx in duadigit:
                    total += rom[idx]
                print(f"\tAngka Desimal dari Angka Romawi {angka} adalah {total}.\n")
                loop = lanjut2(program)
            except:
                print("\t\t** Input yang Anda masukkan salah.")
                loop = lanjut2(program)

def hitunghari():
    hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
    program = "Program Hitung Hari"
    print("\t" + "=" * 20)
    print("\tProgram Hitung Hari")
    print("\t" + "=" * 20)
    loop = True
    while loop:
        try: 
            input_hari = input("\n\tMasukkan nama hari: ").lower()
            # Kondisi hari Jum'at
            if input_hari == 'jumat':
                input_hari = "jum'at"
            # Jika input_hari ada di dalam variabel hari
            if input_hari in hari:
                jumlah = int(input("\tMasukkan jumlah hari: "))
                if (abs(jumlah) + hari.index(input_hari)) < len(hari):
                    print("\t" + str(jumlah) + " hari dari hari " + input_hari.capitalize() + " adalah hari " + (hari[jumlah + hari.index(input_hari)]).capitalize())
                else:
                    print("\t" +  str(jumlah) + " hari dari hari " + input_hari.capitalize() + " adalah hari " + (hari[(round(jumlah % len(hari)) + hari.index(input_hari)) % len(hari)]).capitalize())
                # loop = lanjut2(program)
            else:
                print("\t\t** Nama hari yang Anda masukkan salah.")
            loop = lanjut2(program)

        # Jika input_hari tidak ada di dalam variabel hari
        except:
            print("\t\t** Nama hari yang Anda masukkan salah.")
            loop = lanjut2(program)

def kamushari(): #otomatis
    hari = {
        "senin": "monday",
        "selasa": "tuesday", 
        "rabu": "wednesday",
        "kamis": "thursday",
        "jum'at": "friday",
        "sabtu": "saturday", 
        "minggu": "sunday"
        }
    print("\t" + "=" * 40)
    print("\tKAMUS HARI IND - ENG dan ENG - IND")
    print("\t" + "=" * 40)
    program = "Program Kamus Hari (IND - ENG dan ENG - IND)"
    loop = True
    while loop:
        try:
            pilih = input("\tMasukkan hari (Input Day):").lower()
            # pilih = int(input("\n\tPilih Translate Hari:\n\t1. IDN - ENG\n\t2. ENG - IDN\n\t3. Exit\n\tMasukkan Pilihan: "))
            hariIDN = hari.keys()
            hariENG = hari.values()
            if pilih in hariIDN:
                print(f"\tNama hari {pilih.capitalize()} dalam bahasa Inggris adalah {hari[pilih].capitalize()}.\n")
            elif pilih in hariENG:
                for hariInd, hariEng in hari.items():  
                    if pilih == hariEng:
                        print(f"\tThe day of {pilih.capitalize()} in bahasa is {hariInd.capitalize()}.\n")
            else:
                print("\n\tHari yang dimasukkan salah (Wrong day input)\n")
            loop = lanjut2(program)
        except:
            print("\t\t** Input yang Anda masukkan salah / Wrong Input.\n")
            loop = lanjut2(program)
                
def caesar_chiper():
    print("\t" + "=" * 40)
    print("\tProgram Caesar Chiper")
    print("\t" + "=" * 40)
    program = "Program Caesar Chiper"
    loop = True 
    while loop:
        try:
            kata = input("\tMasukkan kata: ").lower()
            angka = int(input("\tMasukkan angka: "))
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
                print(f"\tKata berjumlah {angka} dari {kata} adalah {hasil}.")
            else:
                print("\t\t** Input yang Anda masukkan salah.")
            loop = lanjut2(program)
        except:
            print("\t\t** Input Angka yang Anda masukkan salah.")
            loop = lanjut2(program)

def konversijumlahhari():
    loop = True
    program = "Program Konversi Jumlah Hari"
    print("\t" + "=" * 20)
    print("\tKONVERSI JUMLAH HARI")
    print("\t" + "=" * 20)
    while loop:
        try:
            x = int(input("\n\tMasukkan jumlah hari: "))
            tahun = x // 360
            bulan = (x % 360) // 30
            minggu = (x % 360 - (bulan * 30)) // 7
            hari = (x % 360 - (bulan * 30)) % 7
            if x >= 0:
                print(f'\t{x} hari = {tahun} tahun, {bulan} bulan, {minggu} minggu, {hari} hari')
                print()
            else:
                print("\t\t** Input yang Anda masukkan salah. Input Angka hanya boleh bernilai Positif.")
            loop = lanjut2(program)
        except:
            print("\t\t** Input jumlah hari yang Anda masukkan salah.")
            loop = lanjut2(program)
            
def faktorial():
    from functools import reduce
    program = "Program Faktorial"
    print("\t" + "=" * (len(program) + 5))
    print("\tProgram Faktorial")
    print("\t" + "=" * (len(program) + 5))
    loop = True
    while loop:
        angka = input("\tMasukkan Angka Anda: ")
        if not angka.isdigit() or int(angka) < 0:
            print("\t\t** Input yang Anda masukkan salah. Input Angka yang dimasukkan harus berupa Angka Positif.")
        else:
            if angka == '0':
                faktorial = 1
            else:
                faktorial = reduce(lambda x, y: x * y, [*range(1, int(angka) + 1)])
            print("\tFaktorial dari angka " + str(angka) + " adalah " + str(faktorial) + '.')
        loop = lanjut2(program)

def fib():
    from functools import reduce
    print("\t" + "=" * 30)
    print("\tPROGRAM FIBONACCI")
    print("\t" + "=" * 30)
    program = "Program Fibonacci"
    loop = True
    while loop:
        try:
            jumlah = int(input("\tMasukkan rentang fibonacci: "))
            a = 0
            b = 1
            deret = [a, b]
            for i in range(2, jumlah):      
                c = a + b
                a = b
                b = c
                deret.append(c)
            if jumlah <= 0:
                print("\t\t** Input yang Anda masukkan salah. Input Angka harus berupa Angka Positif.")
            elif jumlah == 1:
                print(f"\t{jumlah} deret bilangan Fibonacci: {deret[0]}")
                print(f"\tJumlah total {jumlah} deret pertama bilangan Fibonacci: {deret[0]}")
            else:
                print(f"\t{jumlah} deret bilangan Fibonacci: {deret}")
                hasil = reduce(lambda x, y: x + y, deret)
                print(f"\tJumlah total {jumlah} deret pertama bilangan Fibonacci: {hasil}")
            loop = lanjut2(program)
        except:
            print('\t\t** Input yang Anda masukkan salah')
            loop = lanjut2(program)

def tampildatauser():
    import json
    with open('Tugas_Kelompok/datausers.json') as json_file:
        data = json.load(json_file)
    print("\t" + "=" * 50)
    print("\tDATA USERS (USER ID DAN PASSWORD)")
    print("\t" + "=" * 50)
    for idx, user in enumerate(data['datauser'], start=1):
        print("\t" + str(idx) + ") userid: " + user['userid'] + ", password: " + user['password'])
    print("\n\t** Selesai Menampilkan data users **\n")

def lanjut():
    loop2 = True
    while loop2:
        lanjut = input("\t\t* Ingin melanjutkan (Y/N)? ").lower()
        if lanjut == 'n':
            loop2 = False
            loop = False
        elif lanjut != 'y':
            print("\t\tPilih Y atau N.")
        else:
            loop2 = False
            loop = True
    return loop

def lanjut2(program=''):
    loop2 = True
    while loop2:
        lanjut = input(f"\t\t** Ingin melanjutkan {program} (Y/N)? ").lower()
        if lanjut == 'n':
            print(f"\t\t** Keluar dari {program}\n")
            loop2 = False
            loop = False
        elif lanjut != 'y':
            print("\t\t** Pilih Y atau N.")
        else:
            loop2 = False
            loop = True
    return loop

##################################################################################
# PROGRAM UTAMA
##################################################################################

def teamAssignment():
    import json 
    from toko_buah_crud import toko_buah

    datapersonal = {
        'nama': '',
        'userid': '',
        'password':'',
        'email': '',
        'gender': '',
        'usia': '',
        'pekerjaan': '',
        'hobi': '',
        'alamat': '',
        'namakota': '',
        'rt': '',
        'rw': '',
        'zipcode': '',
        'geo': {
            'lat': '',
            'long': ''
        },
        'nohp': ''
    }

    lengkap = 0
    loop = True 
    menu = "MENU UTAMA"
    greet = "|| SELAMAT DATANG DI APLIKASI ||"
    while loop:
        print()
        print("=" * len(greet))
        print(greet)
        print("=" * len(greet))
        print()
        print('-' * len(menu))
        print(menu)
        print('-' * len(menu))
        print("1) Login\n2) Register\n3) Keluar (Exit)")
        pilihmenu = input("Pilih Menu: ")
        print()

        if pilihmenu == '1':
            print("\t** Pilihan Menu Anda: 1 (Login)\n")
            print("\t" + "=" * 50)
            print("\t[LOGIN] Masukkan User ID dan Email Anda.")
            print("\t" + "=" * 50)
            print()

            loopLoginLuar = 3
            waktu = 1
            while waktu <= loopLoginLuar:
                userid = input("\tMasukkan User ID: ")
                password = input("\tMasukkan Password: ")
                if login(userid, password) == True:
                    print("\n\t\t** Anda Berhasil Login.\n")

                    loopLogin = True 
                    while loopLogin:
                        print()
                        print("=" * 30)
                        print("\tPILIHAN MENU")
                        print("=" * 30)
                        print("\n1) Data Personal\n2) Konversi Kode Morse\n3) Kalkulator\n4) Konversi Romawi")
                        print("5) Hitung Hari\n6) Kamus Hari (ENG - IND & IND - ENG)\n7) Caesar Chiper")
                        print("8) Konversi Jumlah Hari\n9) Nilai Faktorial\n10) Jumlah Angka Fibonacci\n11) Data User\n12) Aplikasi Data Buah-buahan\n13) Keluar (Sign Out)")
                        pilihmenu = input("Masukkan pilihan menu Anda: ")
                        print()

                        if pilihmenu == '1':
                            user = datauser(userid, password)
                            print("\t" + "-" * 40)
                            print("\tDATA ANDA")
                            print("\t" + "-" * 40)
                            for k, v in user.items():
                                if k == 'geo':
                                    for a, b in user[k].items():
                                        if a == 'lat':
                                            print("\tLatitude:", b)
                                        else:
                                            print("\tLongitude:", b)
                                elif k == 'hobi':
                                    print("\t" + k.title() + " : " + ", ".join(v).title())
                                elif k == 'userid' or k == 'password' or k =='email':
                                    print("\t" + k.title() + " : " + v)
                                elif k == 'nohp':
                                    print("\tNo. Handphone : " + v)
                                elif k == 'namakota':
                                    print("\tKota : " + v.title())
                                else:
                                    print("\t" + k.title() + " : " + v.title())
                            print("\t" + "-" * 40)
                            print("\t** Selesai Menampilkan data **")
                            print("\t" + "-" * 40 + "\n")
                        elif pilihmenu == '2':
                            kodemorse()
                        elif pilihmenu == '3':
                            kalkulator()
                        elif pilihmenu == '4':
                            romawi()
                        elif pilihmenu == '5':
                            hitunghari()
                        elif pilihmenu == '6':
                            kamushari()
                        elif pilihmenu == '7':
                            caesar_chiper()
                        elif pilihmenu == '8':
                            konversijumlahhari()
                        elif pilihmenu == '9':
                            faktorial()
                        elif pilihmenu == '10':
                            fib()
                        elif pilihmenu == '11':
                            tampildatauser()
                        elif pilihmenu == '12':
                            toko_buah()
                        elif pilihmenu == '13':
                            loopA = True
                            while loopA:
                                pilihmenu = input("\n\tAnda yakin ingin keluar (Y/N)?").lower()
                                if pilihmenu == 'n':
                                    loopA = False
                                elif pilihmenu != 'y':
                                    print("\t\t** Pilih Y atau N.")
                                else:
                                    print("\n\t" + "-" * 30)
                                    print("\t** Sign Out from the Program")
                                    print("\t" + "-" * 30)
                                    print("\n\t\tThank You")
                                    print("\t\tGood Bye ")
                                    print("\t" + "-" * 30)
                                    loopA = False
                                    loopLogin = False
                                    waktu = 10
                        else:
                            print("\t** Pilihan yang Anda masukkan salah.")
                            # loop = lanjut2()

                elif login(userid, password) == 'password':
                    waktu += 1
                    print("\t\t** Password yang Anda masukkan salah.")
                elif login(userid, password) == 'userid':
                    waktu += 1
                    print("\t\t** User ID yang Anda masukkan salah.")
                else:
                    waktu += 1
                    print("\t\t** User ID dan Password yang Anda masukkan belum terdaftar.\n\t\t** Silahkan Register terlebih dahulu.")

                if waktu <= loopLoginLuar:
                    print("\t\t** Anda mempunyai " + str(loopLoginLuar - waktu + 1) + " kesempatan lagi untuk login.\n")
                elif waktu == 4:
                    print("\t\t** Maaf Anda telah " + str(waktu - 1) + " kali gagal login. Silahkan kembali ke Menu Utama.\n")
                # loop = False 

        elif pilihmenu == '2':
            print("\t** Pilihan Menu Anda: 2 (Register)")
            print("\t" + "=" * 50)
            print("\t[REGISTER] Masukkan Data Pribadi Anda.")
            print("\t" + "=" * 50)
            print()

            loopNama = True
            # Masukkan Nama
            while loopNama:
                nama = input("\tNama Lengkap: ")
                if nama.replace(" ", "").isalpha():
                    lengkap += 1
                    datapersonal["nama"] = nama.title()
                    loopNama = False
                else:
                    loop3 = True 
                    print("\t\t* Input yang Anda masukkan salah.\n\t\t* Nama Lengkap harus berupa Huruf dan tidak boleh mengandung Angka dan Karakter.")
                    while loop3:
                        lanjut = input("\t\t* Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopNama = False
                            # loopregister = False
                        elif lanjut != 'y':
                            print("\t\tPilih Y atau N.")
                        else:
                            loop3 = False

            loopUserId = True
            # userid
            while loopUserId and datapersonal['nama']:
                try:
                    userid = input("\tMasukkan User ID Anda: ")
                    digit, letter, alnum = 0, 0, 0
                    # citra123
                    for i in userid:
                        if i.isdigit(): #cek digit
                            digit += 1
                        if i.isalpha(): #cek huruf
                            letter += 1
                        if i.isalnum(): #cek tidak ada karakter
                            alnum += 1
                    if digit >= 1 and letter >= 1 and alnum == len(userid):
                        if cekUserId(userid):
                            print("\t\t** User ID telah digunakan. Silakan masukkan User ID yang lain.")
                            loop3 = True 
                            while loop3:
                                lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                                if lanjut == 'n':
                                    loop3 = False
                                    loopUserId = False
                                elif lanjut != 'y':
                                    print("\t\t** Pilih Y atau N.")
                                else:
                                    loop3 = False
                        else:
                            lengkap += 1
                            datapersonal["userid"] = userid
                            loopUserId = False
                    else:
                        loop3 = True 
                        print("\t\t** User ID hanya bisa huruf dan angka.")
                        while loop3:
                            lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                            if lanjut == 'n':
                                loop3 = False
                                loopUserId = False
                            elif lanjut != 'y':
                                print("\t\t** Pilih Y atau N.")
                            else:
                                loop3 = False
                except:
                    print("\t\t** User ID harus kombinasi Huruf dan Angka.")

            loopPassword = True      
            # password
            while loopPassword and datapersonal['userid']:
                password = input("\tMasukkan Password Anda: ")
                lower, upper, angka = 0, 0, 0
                if len(password) >= 8:
                    # Citra123
                    for i in password:
                        if i.isupper():
                            upper += 1
                        elif i.islower():
                            lower += 1
                        elif i.isdigit():
                            angka += 1
                else:
                    print('\t\t** Panjang Password harus 8 Karakter.')

                if datapersonal['userid'] == password:
                    print('\t\t** Password dan User ID tidak boleh sama. Masukkan password yang lain.')
                    loop3 = True
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopPassword = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False
                elif (lower >= 1 and upper >= 1 and angka >= 1 and lower + upper + angka == len(password)):
                    lengkap += 1
                    datapersonal["password"] = password
                    loopPassword = False
                else:
                    loop3 = True 
                    print("\t\t** Password harus mengandung Huruf Kapital, Huruf Kecil dan Angka (Minimal 8 Karakter).")
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopPassword = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopEmail = True
            # email
            while loopEmail and datapersonal["password"]:
                try:
                    email = input("\tMasukkan alamat Email: ")
                    emailsplit = email.split('@')

                    namauser = emailsplit[0]
                    hosting = emailsplit[-1].split('.')[0]
                    ekstensi = emailsplit[-1].split('.')[1]
                    salah = 0

                    # namauser validation: huruf, angka, underscore, titik
                    for i in range(0, len(namauser)):
                        if "" in emailsplit:
                            print("\t\t** Format username yang Anda masukkan salah.")
                            salah += 1
                            break

                        if not((namauser[i] >= '1' and namauser[i] <= '9') or (namauser[i] >= 'a' and namauser[i] <= 'z') or \
                            (namauser[i] >= 'A' and namauser[i] <= 'Z') or namauser[i] == '.' or namauser[i] == '_'):
                            salah += 1
                            print("\t\t** Format username yang Anda masukkan salah.")
                            break

                    # namahosting validation: hanya boleh huruf dan angka
                    for i in range(0, len(hosting)):
                        if not(hosting[i].isalnum()) or "" in emailsplit[-1].split('.'):
                            salah += 1
                            print("\t\t** Format hosting yang Anda masukkan salah.")
                            break

                    # ekstensi validation: hanya boleh huruf dan maksimal 5 karakter .com .co .id 
                    for i in range(0, len(ekstensi)):
                        if "" in emailsplit[-1].split('.'):
                            print("\t\t** Format ekstensi yang Anda masukkan salah.")
                            salah += 1
                            break
                        else:
                            if not(ekstensi[i].isalpha() and len(ekstensi) <= 5):
                                print("\t\t** Format ekstensi yang Anda masukkan salah.")
                                salah += 1
                                break

                    if salah == 0:
                        # print("\nAlamat Email yang Anda masukkan valid.\n")
                        lengkap += 1
                        datapersonal["email"] = email
                        loopEmail = False
                    else:
                        loop3 = True
                        while loop3:
                            lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                            if lanjut == 'n':
                                loop3 = False
                                loopEmail = False
                            elif lanjut != 'y':
                                print("\t\t** Pilih Y atau N.")
                            else:
                                loop3 = False
                except:
                    print("\n\t\t** Alamat E-mail yang Anda masukkan tidak valid (tidak ada '@' atau '.')\n")
                    loop3 = True
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopEmail = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopGender = True      
            # gender
            while loopGender and datapersonal['email']:
                print("\tPilih Gender Anda:\n\t\t1) Laki-laki\n\t\t2) Perempuan")
                gender = input("\tPilihan Gender: ")
                if gender == '1':
                    lengkap += 1
                    datapersonal["gender"] = 'Laki-laki'
                    loopGender = False
                elif gender == '2':
                    lengkap += 1
                    datapersonal["gender"] = 'Perempuan'
                    loopGender = False
                else:
                    loop3 = True 
                    print("\t\t** Pilih Angka 1 untuk Laki-laki atau Angka 2 untuk Perempuan.")
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopGender = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopUsia = True      
            # usia
            while loopUsia and datapersonal['gender']:
                usia = input("\tMasukkan Usia Anda: ")
                if usia.isdigit():
                    lengkap += 1
                    datapersonal["usia"] = usia
                    loopUsia = False
                else:
                    loop3 = True 
                    print("\t\t** Usia hanya bisa berupa Angka.")
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopUsia = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopPekerjaan = True      
            # pekerjaan
            while loopPekerjaan and datapersonal["usia"]:
                pekerjaan = input("\tMasukkan Pekerjaan Anda: ")
                if pekerjaan.replace(" ", "").isalpha():
                    lengkap += 1
                    datapersonal["pekerjaan"] = pekerjaan
                    loopPekerjaan = False
                else:
                    loop3 = True 
                    print("\t\t** Input pekerjaan yang Anda masukkan salah.\n\t\t** Input Pekerjaan hanya bisa berupa Huruf.")
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopPekerjaan = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopHobi = True      
            # hobi
            while loopHobi and datapersonal["pekerjaan"]:
                # hobi = input("\tMasukkan Hobi Anda: ") #mandi, 
                hobi = input("\tMasukkan Hobi Anda: (Boleh masukkan lebih dari 1, pisahkan dengan tanda ','): ") #mandi, 
                hobbies = hobi.replace(" ", "").split(',') #pengecekan
                hobbies2 =hobi.split(',')
                # ["memasak", "mancing", "maingame", "main123"]
                jumlahhobi = 0
                for i in hobbies:
                    if i.isalpha():
                        jumlahhobi += 1
                if len(hobbies) == jumlahhobi:
                    lengkap += 1
                    datapersonal['hobi'] = hobbies2
                    loopHobi = False
                else:
                    loop3 = True 
                    print("\t\t** Input Hobi yang Anda masukkan salah.\n\t\tInput Hobi hanya bisa berupa Huruf.")
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopPekerjaan = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopAlamat = True      
            # alamat
            while loopAlamat and len(datapersonal["hobi"]) != 0:
                alamat = input("\tMasukkan Alamat Anda: ")
                if (alamat.replace(" ", "").isalnum()) or ('.' in alamat) or ('/' in alamat):
                    lengkap += 1
                    datapersonal["alamat"] = alamat
                    loopAlamat = False
                else:
                    loop3 = True 
                    print("\t\t** Input Alamat yang Anda masukkan salah.\n\t\t** Input Alamat hanya bisa berupa Huruf.")
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopAlamat = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopKota = True      
            # nama kota
            while loopKota and datapersonal["alamat"]:
                kota = input("\tMasukkan Kota Anda: ")
                kotalower = kota.lower().replace(" ", "") #kota lower() dan tanpa spasi

                new_list_kota = []
                for nama_kota in namakota:
                    namakotalower = nama_kota.replace(" ", "").lower()
                    if kotalower in namakotalower:
                        new_list_kota.append(nama_kota)

                namakotalower = map(lambda x: x.replace(" ", "").lower(), namakota)

                if len(new_list_kota) == 1 and (kotalower in namakotalower):
                    datapersonal['namakota'] = kota
                    loopKota = False
                elif len(new_list_kota) >= 1:
                    print('\t\tApakah Kota yang Anda maksud: ' + ', '.join(new_list_kota) + '?')
                else:
                    print("\t\t** Input Nama Kota yang Anda masukkan salah.")
                    loop3 = True
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopKota = False
                            break
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False
                            break
            
            loopRTRW = True
            # RT dan RW
            while loopRTRW and datapersonal['namakota']:
                loopRT = True
                while loopRT:
                    rt = input("\tMasukkan RT: ")
                    if rt.isdigit():
                        lengkap += 1
                        datapersonal['rt'] = rt
                        loopRT = False
                        # loopRTRW = False
                    else:
                        print("\t\t** Input RT yang Anda masukkan salah. RT harus dalam bentuk Angka.")
                        loop3 = True
                        while loop3:
                            lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                            if lanjut == 'n':
                                loop3 = False
                                loopRT = False
                                loopRTRW = False
                            elif lanjut != 'y':
                                print("\t\t** Pilih Y atau N.")
                            else:
                                loop3 = False
                                # loopRT = False
                loopRW = True
                while loopRW:
                    rw = input("\tMasukkan RW: ")
                    if rw.isdigit():
                        lengkap += 1
                        datapersonal['rw'] = rw 
                        loopRW = False
                        loopRTRW = False
                    else:
                        print("\t\t** Input RW yang Anda masukkan salah. RW harus dalam bentuk Angka.")
                        loop3 = True
                        while loop3:
                            lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                            if lanjut == 'n':
                                loop3 = False
                                loopRW = False
                                loopRTRW = False
                            elif lanjut != 'y':
                                print("\t\t** Pilih Y atau N.")
                            else:
                                loop3 = False
                                # loopRW = False

            loopZipCode = True
            while loopZipCode and datapersonal['rw']:
                zipcode = input("\tMasukkan Kodepos: ")
                if zipcode.isdigit() and len(zipcode) == 5:
                    lengkap += 1
                    datapersonal['zipcode'] = zipcode
                    loopZipCode = False
                else:
                    print("\t\t** Kodepos yang Anda masukkan salah.")
                    loop3 = True
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopLat = False
                            loopGeo = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False
    

            loopGeo = True
            # Geo: Latitude dan Longitude
            while loopGeo and datapersonal['zipcode']:
                try:
                    loopLat = True
                    while loopLat:
                        lat = input("\tMasukkan Latitude: ")

                        if isinstance(float(lat), float) or isinstance(int(lat), int):
                            if (-90 <= float(lat) <= 90):
                                lengkap += 1
                                datapersonal['geo']['lat'] = lat 
                                loopLat = False
                            else:
                                print("\t\t** Nilai Latitude harus diantara -90 dan 90.")
                                loop3 = True
                                while loop3:
                                    lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                                    if lanjut == 'n':
                                        loop3 = False
                                        loopLat = False
                                        loopGeo = False
                                    elif lanjut != 'y':
                                        print("\t\t** Pilih Y atau N.")
                                    else:
                                        loop3 = False
                    loopLong = True
                    while loopLong:
                        long = input("\tMasukkan Longitude: ")
                        if isinstance(float(long), float) or isinstance(int(long), int):
                            if (-180 <= float(long) <= 180):
                                lengkap += 1
                                datapersonal['geo']['long'] = long
                                loopLong = False 
                                loopGeo = False
                            else:
                                print("\t\t** Nilai Longitude harus diantara -180 dan 180.")
                                loop3 = True
                                while loop3:
                                    lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                                    if lanjut == 'n':
                                        loop3 = False
                                        loopLong = False
                                        loopGeo = False
                                    elif lanjut != 'y':
                                        print("\t\t** Pilih Y atau N.")
                                    else:
                                        loop3 = False
                        # loopGeo = False
                except:
                    print("\t\t** Input Latitude/Longitude yang Anda masukkan salah.")  
                    loop3 = True
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopGeo = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False

            loopNoHp = True 
            # no Handphone
            while loopNoHp and datapersonal['geo']['lat']:
                nohp = input("\tMasukkan No. Handphone Anda: ")
                if nohp.isdigit() and 9 <= len(nohp) <= 13: # len maks. 13 min. 9
                    lengkap += 1
                    datapersonal['nohp'] = nohp 
                    loopNoHp = False 
                else:
                    print("\t\t** Input Nomor Handphone yang Anda masukkan salah.")  
                    loop3 = True
                    while loop3:
                        lanjut = input("\t\t** Ingin melanjutkan (Y/N)? ").lower()
                        if lanjut == 'n':
                            loop3 = False
                            loopNoHp = False
                        elif lanjut != 'y':
                            print("\t\t** Pilih Y atau N.")
                        else:
                            loop3 = False
                        
            # print(datapersonal)
            # print(lengkap)

            if lengkap == 15:
                print()
                print("\tDATA ANDA")
                print('\tNama Lengkap:', datapersonal['nama'])
                print('\tE-mail:', datapersonal['email'])
                print('\tGender:', datapersonal['gender'])
                print('\tUsia:', datapersonal['usia'])
                print('\tPekerjaan:', datapersonal['pekerjaan'])
                print('\tHobi:', ', '.join(datapersonal['hobi']))
                print('\tAlamat:', datapersonal['alamat'])
                print('\tKota:', datapersonal['namakota'])
                print('\tKodepos:', datapersonal['zipcode'])
                print('\tRT:', datapersonal['rt'], 'RW: ', datapersonal['rw'])
                print('\tGeo --> lat:', datapersonal['geo']['lat'], ', long:', datapersonal['geo']['long'])
                print('\tNo. Handphone:', datapersonal['nohp'])
                print()
                loopSimpan = True
                while loopSimpan:
                    simpan = input("\tApakah Anda akan menyimpan data Anda (Y/N): ").lower()
                    if simpan == 'n':
                        print('\t\t** Data tidak berhasil disimpan.')
                        loopSimpan = False
                    elif simpan != 'y':
                        print("\t\t** Input yang Anda masukkan salah.")
                    else:
                        print("\t\t** Data berhasil disimpan.")
                        # datas.append(datapersonal)
                        # Python program to update 
                        
                        # Fungsi untuk menambah data ke Tugas_Kelompok/Tugas_Kelompok/datausers.json
                        def write_json(data, filename='Tugas_Kelompok/datausers.json'): 
                            with open(filename,'w') as f: 
                                json.dump(data, f, indent=4) 
                            
                        with open('Tugas_Kelompok/datausers.json') as json_file: 
                            data = json.load(json_file) 
                            # append datapersonal ke data['datauser'] di Tugas_Kelompok/datausers.json
                            data['datauser'].append(datapersonal)
                        
                        write_json(data)

                        loopSimpan = False
            else:
                print("\t\t** Data tidak berhasil disimpan.")
            
            # loop = False

        elif pilihmenu == '3':
            print("\t** Pilihan Menu Anda: 3 (Exit Menu)\n")
            print("\t" + "=" * 30)
            print("\t\tTerima Kasih")
            print("\t" + "=" * 30)
            loop = False
        
        else:
            print("\t" + "-" * 40)
            print("\t** Pilihan Menu yang Anda Masukkan salah.")
            print("\t** Silahkan pilih Menu 1, 2 atau 3.")
            print("\t" + "-" * 40 + "\n")


teamAssignment()