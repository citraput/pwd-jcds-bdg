#########################################################################
# Soal 1
#########################################################################
# Sembilan belas tahun yang lalu umur anak setengah tahun lebih muda dari 
# seperempat umur ibunya. umur anak sekarang 19 tahun lebih tua dari 
# sepertujuh umur ibunya
# output: umur ibu saat melahirkan anaknya adalah

# Persamaan 1: Umur_anak - 19 = 1/4 * (Umur_ibu -19) - 1/2 
# Persamaan 2: Umur_anak = 19 + (1/7 * Umur_ibu)
# angka 19 --> x
x = 19 # perbedaan tahun dari umur anak dan ibu
# angka 1/4 --> y
y = 1/4 # perbandingan umur ibu
# angka 1/2 --> z
z = 1/2 # perbedaan tahun
# angka 1/7 --> c
c = 1/7

# Persamaan 1 menjadi:
# Umur_anak - 19 = 1/4 * (Umur_ibu -19) - 1/2
# Umur_anak - x = y * (Umur_ibu - x) - z
# Umur_anak - x = (y * Umur_ibu) - (y * x) - z
# Umur_anak - (y * Umur_ibu) = x - (x * y) - z

# Persamaan 2 menjadi:
# Umur_anak = 19 + (1/7 * Umur_ibu)
# Umur_anak = x + (c * Umur_ibu)
# Umur_anak - x = c * Umur_ibu
# Umur_ibu = (Umur_anak - x) / c

# Substitusi ke persamaan 1:
# Umur_anak - (y * Umur_ibu) = x - (x * y) - z
# Umur_anak - (y * (Umur_anak - x)/c) = x - (x * y) - z
# Umur_anak - (y * Umur_anak / c) + (x * y / c) = x - (x * y) - z
# (c * Umur_anak) - (y * Umur_anak / c) + (x * y / c) = c(x - (x * y) - z)
# (Umur_anak * (c - y)) + (x * y) =  c(x - (x * y) - z)
# Umur_anak = (c(x - (x * y) - z) - (x * y)) / (c - y)
umur_anak = (c * (x - (x * y) - z) - (x * y)) / (c - y)
print("Umur Anak:", round(umur_anak))

umur_ibu = (umur_anak - x) / c
print("Umur Ibu:", round(umur_ibu))

print('Umur ibu saat melahirkan:', round(umur_ibu - umur_anak))


#########################################################################
# Soal 2 
#########################################################################
# jumlah umur Andi dan umur ayahnya skr adalah 50 tahun
# 4 tahun yang lalu umur ayah andi 6 kali umur Andi
# output: umur andi dan umur ayah saat ini adalah:

# Persamaan 1: umur_andi + umur_ayah = 50
# Persamaan 2: umur_ayah - 4 = 6 * (umur_andi - 4)
# Pertambahan umur ayah dan andi
x = 50
# Empat tahun yang lalu
y = 4
# Perbandingan umur ayah dan andi 4 tahun yang lalu
z = 6

# Persamaan 1: umur_andi + umur_ayah = 50
# atau sama dengan: umur_andi + umur_ayah = x
# Persamaan 2: umur_ayah - 4 = 6 * (umur_andi - 4)
# atau sama dengan: umur_ayah - y = z * (umur_andi - y)
# umur_ayah = z * (umur_andi - y) + y

# Substitusi persamaan 1 dan 2
# umur_andi + umur_ayah = x
# umur_andi + z * (umur_andi - y) + y = x
# umur_andi + z * umur_andi - z * y  + y = x
# umur_andi * (1 + z) - y * z + y = x
# umur_andi * (1 + z) = x - y + y * z
# umur_andi = (x - y + (y * z)) / (1 + z)
umur_andi = (x - y + (y * z)) / (1 + z)
print("Umur Andi:", round(umur_andi))
umur_ayah = x - umur_andi
print("Umur Ayah:", round(umur_ayah))
