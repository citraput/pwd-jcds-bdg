minimum = int(input("Masukkan bilangan minimum: "))
maksimum = int(input("Masukkan bilangan maksimum: "))

# Genap: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
A = set(list(filter(lambda x: x % 2 == 0, range(minimum + 1, maksimum + 1))))
print(A)

# Ganjil: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
B = set(list(filter(lambda x: x % 2 != 0, range(minimum, maksimum + 1))))
print(B)

# Bilangan Negatif > -20: {-19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1}
C = set([x for x in range(-maksimum + 1, 0)])
print(C)

# Bilangan Prima: {2, 3, 5, 7, 11, 13, 17, 19}
# D = [i for i in range(2, maksimum + 1) if i == 2 or i == 3 or (i % 2 != 0 and i % 3 != 0)]
D = set(list(filter(lambda x: x == 2 or x == 3 or (x % 2 != 0 and x % 3 != 0), range(2, maksimum + 1))))
print(D)

# for num in range(minimum, maksimum + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# Bilangan Komposit: {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}
E = set(list(filter(lambda x: x != 2 and x != 3 and (x % 2 == 0 or x % 3 == 0), range(minimum, maksimum + 1))))
print(E)

# a) A U B U C U D U E 
print("a: ", A.union(B).union(C).union(D).union(E))
# b) (A n B) U (D n E)
print("b: ", (A.intersection(B)).union(D.intersection(E)))
# c) ( A U B ) n (D U E)
print("c: ", (A.union(B)).intersection(D.union(E)))
# d) (A U B) - (D U E)
print("d: ", (A.union(B)).difference(D.union(E)))
# e) (A U B U C) - (A n E)
print("e: ", (A.union(B).union(C)).difference(A.intersection(E)))