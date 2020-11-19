### ==== Team Assignment === Present Jumat : Tim min 2 - 3
### CRUD == Create, Read, Update, Delete
# Membuat aplikasi mini (untuk data barang)
# ada menu:
# 1. Cetak isi daftar barang 
# 2. Menambah Data ke daftar barang (Create)
# 3. Menghapus data dari daftar barang (Delete)
# 4. Mengubah data dalam daftar barang (Update)
# 5. Exit (keluar)

# Kondisi:
# 1. Read (Cetak data)
# - Jika tidak ada data, keluar notif: Daftar Barang masih kosong
# - Cetak seluruh isi daftar barang 
# 2. Create (Tambah Data)
# - Pengecekan jenis data: angka ? notif --> Data yang Anda Masukkan salah
# - Pengecekan duplikasi: jika sudah ada: keluar notif pilihan --> "Data sudah ada sebelumnya, apakah tetap akan disimpan? (Y/N)"
# - Y: Data tersimpan, N: Data Tidak tersimpan
# - Data langsung disimpan dan keluar notif: Data Tersimpan 
# 3. Delete (Hapus Data)
# - Jika data yang diminta user tidak ada, keluar notif: Nama Barang Tidak ada
# - Hapus seluruh data sesuai yang diminta user, jeruk dua2nya dihapus
# 4. Update (Ubah Data)
# - Jika data yang diminta user tidak ada, keluar notif: Nama Barang tidak ada
# - Update datanya contoh: jeruk -- ubah jadi jeruk bali
# - keluar notif: Data terupdate
# 5. Exit (Keluar Aplikasi)
# - Selama user belum memilih opsi ini, Menu akan terus ditampilkan
def toko_buah():
    daftarbarang = ["jeruk", "apel", "jeruk", "nanas", "semangka", "melon"]
    # daftarbarang = []
    fruits = ["jeruk", "apel", "anggur", "pear", "alpukat", "avocado", 
    "belimbing", "bengkuang", "blueberry", "blackberry", "cempedak", 
    "ceri", "delima", "duku", "durian", "jambu", "jambu air", "jambu batu",
    "jambu bol", "jambu biji", "jeruk bali","jeruk bandung", "jeruk purut", "jeruk nipis",
    "kedongdong", "kelapa", "lengkeng", "kersen", "kiwi", "kismis", "kurma",
    "lemon", "leci", "limau", "labu","mangga", "manggis", "markisa", "melon",
    "mengkudu", "mentimun", "mentimun suri", "nanas", "nangka", "naga", "paprika",
    "pepaya", "pisang", "rambutan", "raspberry", "salak", "sawo", "semangka",
    "sirsak", "srikaya", "strawberry", "sukun", "terong", "timun", "tomat", 
    "ubi", "waluh"]

    greet = "**  SELAMAT DATANG DI APLIKASI DATA BARANG  **"
    menu = ["Cetak isi daftar barang", "Menambah data ke daftar barang", "Menghapus data dari daftar barang", "Mengubah data dalam daftar barang", "Keluar (Exit)"]

    print()
    print('*' * len(greet))
    print('**' + ''.ljust(len(greet) - 4) + '**')
    # print('**'.rjust(10))
    print(greet)
    print('**' + ''.ljust(len(greet) - 4) + '**')
    print('*' * len(greet))
    print()

    exitmenu = False 

    while not exitmenu:
        # Tampilan Menu
        # for i in range(1, 4):
        #     print(''.rjust(18) + ' * ' * 3)
        # z = ''
        # for a in range(1, 4):
        #     for c in range(1, 5 + a):
        #         z += '   '
        #     for b in range(0, 7 - (2 * a)):
        #         z += ' * '
        #     z += '\n'
        # print(z)

        print()
        print("-" * len(greet))
        print("**  " + "Menu".center(36) + '**'.rjust(6))
        print("-" * len(greet))

        # Table Menu
        for idx, name in enumerate(menu):
            print('|'.ljust(2) + str(idx + 1) + '. |  ' + name + " " * (37 - len(name)) + '|')
        print('|' + '_' * (len(greet) - 2) + '|')
        print()

        try: 
            pilihmenu = int(input("Silahkan masukkan pilihan menu [1 - 5]: "))
            print()

            # 1. READ
            if pilihmenu == 1:
                loop = True
                print("Menu 1 has been selected.\n")
                while loop:
                    c1 = input("Anda yakin ingin mencetak daftar barang (Y/N)? ")
                    print()
                    c1 = c1.lower()

                    # Ingin mencetak daftar barang
                    if c1 == "y" and daftarbarang != []:
                        print("*" * len(greet))
                        print("| "+ "No.| " + "Daftar Barang" + "|".rjust(26))
                        print("*" * len(greet))
                        for idx, barang in enumerate(daftarbarang):
                            # Tampilan Daftar Barang
                            lenidx = len(str(idx) + '.')
                            print("|".ljust(2) + str(idx + 1) + "." + " " * (3 - lenidx) + "|  " + barang.title() + " " * (37 - len(barang)) + "|")
                        print("|" + "_" * (len(greet) - 2) + "|")
                        print()
                        print("+" * len(greet))
                        print()
                        loop = False
                    elif c1 == "y" and daftarbarang == []:
                        print("*" * len(greet))
                        print("| "+ "No.| " + "Daftar Barang" + "|".rjust(26))
                        print("*" * len(greet))
                        notif = "Tidak ada data tersedia"
                        print("|       Tidak ada data tersedia." + " " * (36 - len(notif)) + "|")
                        print("|" + "_" * (len(greet) - 2) + "|")
                        print()
                        print("+" * len(greet))
                        print()
                        loop = False
                    elif c1 == "n":
                        loopA = True
                        while loopA:
                            c2 = input("Ingin kembali ke menu awal (Y/N)? ")
                            c2 = c2.lower()
                            if c2 == "y":
                                loopA = False
                                loop = False
                                exitmenu = False
                            elif c2 == "n":
                                print("="*len(greet))
                                print("\nThank you!!!\n")
                                print("="*len(greet))
                                loopA = False
                                loop = False
                                exitmenu = True
                            else:
                                print("\nInput yang Anda masukkan salah.\n")
                                loopA = True
                    else:
                        print("Input yang Anda masukkan salah.\n")

            # 2. CREATE
            elif pilihmenu == 2:
                print("Menu 2 has been selected.\n")
                loop = True
                while loop:
                    cekdata = input("Silahkan masukkan buah yang akan ditambahkan: ")
                    cekdata = cekdata.lower()
                    cekdatasplit = cekdata.split(" ")
                    awalanbuah = cekdatasplit[0]
                    #Split nama buah nya, biar ketika pengecekan yg di cek hanya nama buah depannya aja
                    if awalanbuah in fruits:
                        if cekdata in daftarbarang:
                            #Dibikin while lagi biar ketika line 151 bukan y atau n loop nya ke 151 lagi bukan 146
                            pool = True
                            while pool:
                                m = input("\nData sudah ada dalam list, tetap ditambahkan (Y/N)? ")
                                m = m.lower()
                                if m == "y":
                                    daftarbarang.append(cekdata)
                                    print("\nData sudah ditambahkan.\n")
                                    #Harus rubah true false nya dari loop while 150
                                    loop = False
                                elif m == "n":
                                    print("\nData tidak ditambahkan.\n")
                                    #Harus rubah true false nya dari loop while 150
                                    loop = False
                                else:
                                    print("\nInput yang Anda masukkan salah.\n")
                        else:
                            daftarbarang.append(cekdata)
                            print("\nData Sudah Ditambahkan.\n")
                            loop = False    
                    else: 
                        print("\nInput yang Anda masukkan bukan buah.\n")
                        
            # 3. DELETE
            elif pilihmenu == 3:
                print("Menu 3 has been selected\n")
                loop = True
                while loop:
                    print("""1. Hapus sebagian data\n2. Hapus seluruh data\n3. Kembali ke Menu Awal""")
                    deldaftar = input("Silahkan pilih menu [1 - 3]: ")
                    if deldaftar == "1": 
                        pildata = input("\nMasukan nama buah yang ingin dihapus : ")
                        pildata = pildata.lower()
                        daftarbarangupdate = []
                        if pildata in daftarbarang:
                            for barang in daftarbarang:
                                if pildata != barang:
                                    daftarbarangupdate.append(barang)
                            daftarbarang = daftarbarangupdate[:]
                            print("\nBarang telah dihapus dari daftar.")
                            print()
                            loop = False
                        else:
                            print("\nNama barang tidak ada di dalam daftar.\n")
                        
                    elif deldaftar == "2":
                        jwb = input("\nAnda yakin ingin menghapus seluruhnya (Y/N)?")
                        jwb = jwb.lower()
                        if jwb == "y":
                            daftarbarang.clear()
                            print("\nData dihapus seluruhnya.\n")
                            loop = False
                        elif jwb == "n":
                            print("\nData tidak dihapus.\n")
                                # loop = False
                        else:
                            print("\nInput yang Anda masukkan salah.\n")
                    elif deldaftar == "3":
                        loop = False
                    else:
                        print("\nInput yang Anda masukkan tidak ada dalam pilihan\n")
                
            # 4. UPDATE
            elif pilihmenu == 4:
                print("Menu 4 has been selected\n")
                run = True
                while run:
                    datalama = input("Silahkan masukan nama buah yg ingin diubah: ")
                    datalama = datalama.lower()
                    # datalama ada di dalam daftar barang
                    if datalama in daftarbarang: 
                        databaru = input("\nSilahkan masukan data buah baru: ")
                        databaru = databaru.lower()
                        daftarbarangbaru = []
                        if databaru in daftarbarang:
                            for barang in daftarbarang:
                                daftarbarangbaru.append(barang.replace(datalama, databaru))  
                                daftarbarang = daftarbarangbaru[:]
                            print(f"\n{datalama.title()} sudah diganti menjadi {databaru.title()}.")
                            run = False
                        else:
                            for barang in daftarbarang:
                                daftarbarangbaru.append(barang.replace(datalama, databaru))  
                                daftarbarang = daftarbarangbaru[:]
                            print(f"\n{datalama.title()} sudah diganti menjadi {databaru.title()}.")
                            run = False
                        # datalama tidak ada di dalam daftar barang
                    else:
                        print("\nNama barang tidak ada di dalam daftar.\n")
                    print()
                # print()

            # 5. EXIT
            elif pilihmenu == 5:
                print("=" * len(greet))
                print("Thank you!!!")
                print("=" * len(greet))
                print()
                exitmenu = True

            # Pilihan bukan 1 - 5
            else:
                print("="*len(greet))
                print("\nInput yang di pilih tidak ada dalam pilihan.\n")
                print("="*len(greet))
        except:
            print("\nPilihan Menu hanya 1 - 5.\n")

toko_buah()