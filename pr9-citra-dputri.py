# Lat 1:
# Buat Algoritma...
# Buat List 
# Pilihan:
# 1 = ascending(a-z) dari kecil ke besar 
# 2 = descending(z-a) dari yang terbesar ke terkecil 
# tidak boleh pake reverse, ::-1, pake algoritma, tidak boleh pake fungsi 
# output: sesuai pilihan 

def ascdesc(pilihan , lst):
    if pilihan == 1:
        for i in range(0, len(lst) - 1):
            minposition = len(lst) - 1
            for j in range(len(lst) - 2, i - 1, -1):
                if lst[j] < lst[minposition]:
                    minposition = j 
            temp = lst[i]
            lst[i] = lst[minposition]
            lst[minposition] = temp
        return lst
    else:
        for i in range(0, len(lst) - 1):
            minposition = len(lst) - 1
            for j in range(len(lst) - 2, i - 1, -1):
                if lst[j] > lst[minposition]:
                    minposition = j 
            temp = lst[i]
            lst[i] = lst[minposition]
            lst[minposition] = temp
        return lst 

# def ascdesc(pilihan):
#     if pilihan == 1:
#         list_asc = []
#         for i in range(97, 123):
#             list_asc.append(chr(i))
#         return list_asc
#     elif pilihan == 2:
#         list_desc = []
#         for i in range(122, 96, -1):
#             list_desc.append(chr(i))
#         return list_desc
#     else:
#         return "Parameter hanya 1 dan 2"

a = ['b', 'g', 'p', 'd', 'a', 'w']   
print(ascdesc(1, a))  
print(ascdesc(2, a)) 

# print(ascdesc(1))
# print(ascdesc(2))

# Lat 2:
# Buat Algoritma 
# Cari Nilai Maksimal dan nilai Minimal 
def minmaks(lst):
    for i in range(0, len(lst) - 1):
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]:
                temp = lst[j]
                lst[j] = lst[j - 1]
                lst[j - 1] = temp
    return f"\nNilai minimal dari list adalah {lst[0]} dan nilai maksimal dari list adalah {lst[-1]}.\n"

a = [8, 4, 6, 1, 9, 2, 0, 4, 8]
print(minmaks(a))

# Lat 3:
# Buat Algoritma
# Buat List 
# cari:
# Modus = nilai yang paling sering muncul 
# Median = nilai tengah
# Mean = rata-rata 
# Q1 = Quartal 1 atau 25%
# Q3 = Quartal 3 atau 75%
# Outliers
def stats(lst):
    lst = sorted(lst)

    # Modus
    newlst = map(lambda x: str(x), lst)
    count = {}
    for i in newlst:
        try:
            if count[i]:
                count[i] += 1
        except:
            count[i] = 1
    max_count = max(count.values())
    temp = []
    for k, v in count.items():
        if v == max_count:
            temp.append(k)
    modus = ', '.join(temp)

    # Median
    idx = len(lst) // 2
    if len(lst) % 2 == 0:
        median = (lst[idx] + lst[idx - 1]) / 2
    else:
        median = lst[idx]

    # Mean
    mean = sum(lst) / len(lst)

    # Quartal 1
    # [1, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5, 6]
    # new_list = sorted(lst)
    idx_q1 = idx // 2
    print(idx_q1)

    q1 = (lst[idx_q1] + lst[idx_q1 - 1]) / 2
    print("q1 ganjil", q1)

    # Quartal 3
    idx_q3 = len(lst) - idx + 1
    q3 = (lst[idx_q3] + lst[idx_q3 + 1]) / 2

    # Outlier
    rangeq3q1 = q3 - q1
    lowerbound = q1 - (1.5 * rangeq3q1)
    upperbound = q3 + (1.5 * rangeq3q1)
    outlier = []
    for i in lst:
        if i < lowerbound or i > upperbound:
            outlier.append(i)
    # outlier = ', '.join(outlier)

    return f"\nList Anda setelah di sorting: {lst}\n\
Modus: {modus}\n\
Median: {median}\n\
Mean: {round(mean, 2)}\n\
Quartal 1: {q1}\n\
Quartal 3: {q3}\n\
Outlier: {outlier}\n"

    # return f"{idx_q3} Modus adalah {modus}, Q1 adalah {q1}, Q3 adalah {q3} {max_count} {count} {lst} {idx} {mean} {median}"

b = [2, 8, 3, 1, 8, 7, 1009, 1001]
c = [2, 7, 3, 3, 1, 8, 7, 4, 2002]
d = [3,4,5,5, 6,6,7,8]
print(stats(b))
print(stats(c))
print(stats(d))

# Lat 4:
# Buat def atau function 
# ada deret angka
# 1 2 3 4 5
# 6 7 8 9
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# input: spin ke: pilihan ke 1-4
# pilihan 1:
# 21 16 11 6 1
# 22 17 12 7 2
# 23 18 13 8 3
# 24 19 14 9 4
# 25 20 15 10 5

# pilihan 2:
# 25 24 23 22 21
# 20 19 18 17 16 
# 15 14 13 12 11
# 10 9 8 7 6
# 5 4 3 2 1

# pilihan 3:
# 5 10 15 20 25
# 4 9 14 19 24
# 3 8 13 18 23
# 2 7 12 17 22
# 1 6 11 16 21

# pilihan 4:
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

def rotasi(x):
    z = ''

    if x == 1:
        for i in range(21, 26):
            for j in range(0, 25, 5):
                z += str(i - j) + ' '
            z += '\n'

    elif x == 2:
        for i in range(25, 0, -5):
            for j in range(i + 1, i - 4, -1):
                z += str(j - 1) + ' '
            z += '\n'

    elif x == 3:
        for i in range(6, 1, -1):
            for j in range(0, 5):
                z += str(i - 1 + (5 * j)) + ' '
            z += '\n'

    elif x == 4:
        for i in range(0, 25, 5):
            for j in range(i, i + 5):
                z += str(j + 1) + ' '
            z += '\n'

    return f"Pilihan {x}\n{z}"


print(rotasi(1))
print()
print(rotasi(2))
print()
print(rotasi(3))
print()
print(rotasi(4))
