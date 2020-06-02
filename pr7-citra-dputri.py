### Email Validation ###
########################

# input:
# Masukkan alamat Email: 

# Kondisi:
# - Memiliki format: nama user@nama hosting.ekstensi
# - Nama user hanya boleh: huruf, angka dan underscore dan titik
# - Nama hosting hanya boleh: huruf dan angka 
# - nama ekstensi hanya boleh huruf dan maksimal 5 karakter .com .co .id

# output: 
# Alamat Email yang Anda masukkan tidak valid 
# - Karena format email salah (tidak ada @ atau pake ,)
# - Karena format user name yang Anda masukkan salah
# - Karena format hosting yang Anda masukkan salah
# - Karena format ekstensi yang Anda masukkan salah

# Alamat Email yang Anda masukkan valid 
# contoh : andre@gmail.com, joni12@city.id, joni234andre@avernger25.space (Valid)
# contoh2: andre-&^john@gmail.com, johny245@g_#^mail.com, 79andi@yahoo, tony@avenger25.community
# citra@yahoo.co.id,  citra@@yahoo.com, citra@yahoo..com, citra@@yahoo.co.id, citra@yahoo..co.id
loop = True
while loop:
    try:
        email = input("Masukkan alamat Email: ")

        # loopEmail = True
        # while loopEmail:
            
        emailsplit = email.split('@')

        namauser = emailsplit[0]
        hosting = emailsplit[-1].split('.')[0]
        ekstensi = emailsplit[-1].split('.')[1]
        salah = 0

        # namauser validation: huruf, angka, underscore, titik
        for i in range(0, len(namauser)):
            if "" in emailsplit:
                print("Format username yang Anda masukkan salah.")
                salah += 1
                break

            if not((namauser[i] >= '1' and namauser[i] <= '9') or (namauser[i] >= 'a' and namauser[i] <= 'z') or \
                (namauser[i] >= 'A' and namauser[i] <= 'Z') or namauser[i] == '.' or namauser[i] == '_'):
                salah += 1
                print("Format username yang Anda masukkan salah.")
                break

        # namahosting validation: hanya boleh huruf dan angka
        for i in range(0, len(hosting)):
            if not(hosting[i].isalnum()) or "" in emailsplit[-1].split('.'):
                salah += 1
                print("Format hosting yang Anda masukkan salah.")
                break

        # ekstensi validation: hanya boleh huruf dan maksimal 5 karakter .com .co .id 
        for i in range(0, len(ekstensi)):
            if "" in emailsplit[-1].split('.'):
                print("Format ekstensi yang Anda masukkan salah.")
                salah += 1
                break
            else:
                if not(ekstensi[i].isalpha() and len(ekstensi) <= 5):
                    print("Format ekstensi yang Anda masukkan salah.")
                    salah += 1
                    break

        if salah == 0:
            print("\nAlamat Email yang Anda masukkan valid.\n")
            loop = False
        else:
            loop3 = True
            while loop3:
                lanjut = input("Ingin melanjutkan (Y/N)? ").lower()
                if lanjut == 'n':
                    loop3 = False
                    # loopEmail = False
                    loop = False
                    # break
                elif lanjut != 'y':
                    print("Pilih Y atau N.")
                else:
                    loop3 = False
                    # loop = Fal

    except:
        print("\nAlamat E-mail yang Anda masukkan tidak valid (tidak ada '@' atau '.')\n")
        loop3 = True
        while loop3:
            lanjut = input("Ingin melanjutkan (Y/N)? ").lower()
            if lanjut == 'n':
                loop3 = False
                # loopEmail = False
                loop = False
                # break
            elif lanjut != 'y':
                print("Pilih Y atau N.")
            else:
                loop3 = False
                # loop = Fal