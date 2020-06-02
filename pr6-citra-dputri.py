# Lat:
# input: masukkan kalimat
# outputnya: kata dalam kalimat dibalik

# input: "nama saya joni"
# output nya: "aman ayas inoj"

kalimat = input("Masukkan kalimat: ")
kalimatreverse = []

for kata in kalimat.split(' '):
    katabaru = ''
    for i in range(len(kata) - 1, -1, -1):
        katabaru += kata[i]
    kalimatreverse.append(katabaru)
print(' '.join(kalimatreverse))

# for i in range(len(kalimat) - 1, -1, -1):
#     kalimatreverse1 += kalimat[i]
# print(kalimatreverse1)

# kalimatreverse2 = ''
# for kata in kalimat[::-1]:
#     kalimatreverse2 += kata
# print(kalimatreverse2)

fruits = []
if len(fruits) == 0:
    print("Daftar masih kosong.")