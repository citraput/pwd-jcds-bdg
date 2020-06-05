def segitigaKata(kata):

    kata = kata.replace(" ", "")

    z = []
    for i in range(0, len(kata)):
        z.append((i * (i + 1)) // 2) # Deret Triangular Number
    # print(z)
    # print(len(kata))

    if len(kata) in z:
        num = 0
        f = ''
        temp = z.index(len(kata))

        for i in range(temp): 
            for j in range(i+1):
                f += kata[num] + ' '
                num += 1  
            f += '\n'
        
        num1 = 0
        for k in range(temp, 0, -1):
            for l in range(1, k +1):
                f += kata[num1] + ' '
                num1 += 1
            f += '\n'
        return f
    else:
        return 'Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.'

# 1, 3, 6, 10, 15, 21, 28, 36, 45, ..
# print(segitigaKata('abc'))
print(segitigaKata('Purwadhika')) #

# P 
# u r     
# w a d   
# h i k a 
# p u r w 0:4
# a d h   4:7
# i k     7:9
# a       9:10

# 1, 3, 6, 10, 15

print(segitigaKata('Purwadhika Startup and Coding School @BDG'))
# P
# u r
# w a d 
# h i k a
# S t a r t
# u p a n d C
# o d i n g S c
# h o o l @ B D G
# P u r w a d h i
# k a S t a r t
# u p a n d C
# o d i n g
# S c h o
# o l @
# B D 
# G



print(segitigaKata('kode python'))
# k
# o d
# e p y
# t h o n
# k o d e
# p y t
# h o
# n
# 
print(segitigaKata('kode'))
print(segitigaKata('kodepythonasika'))
