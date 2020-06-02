# Personal Assignment

# Lat 1:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
print('Latihan 1:')
z = ''
for i in range(1, 6): # 1, 2, 3, 4, 5
    for j in range(i):
        z += str(i) + ' '
    z += '\n'
print(z)
print()

# Lat 2:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("Latihan 2:")
z = ''
for i in range(1, 6): #1, 2, 3, 4, 5
    for j in range(1, i + 1): # 1, 2, 3
        z += str(j) + ' '
    z += '\n'
print(z)
print()

# Lat 3:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
print("Latihan 3: ")
z = ''
for i in range(4, -1, -1):
    # z = ''
    for j in range(5, i, -1): # 5, 6
        z += str(j) + ' '
    # print(z)
    z += '\n'
print(z)
print()

# Lat 4:
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4 
# 5
print("Latihan 4: ")
z = ''
for i in range(1, 6): # 1, 2, 3, 4, 5
    for j in range(6, i, -1): #6, 5, 4, 3, 2
        z += str(i) + ' '
    z += '\n'
print(z)
print()

# Lat 5:
# 1 2 3 4 5\n
# 1 2 3 4
# 1 2 3
# 1 2
# 1
print("Latihan 5:")
z = ''
for i in range(5, 0, -1): # 4, 3, 2, 1 
    for j in range(1, i + 1): # 1, 2, 3, 4
        z += str(j) + ' '
    z += '\n'
print(z)
print()

# Lat 6:
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
print("Latihan 6:")
z = ''
for i in range(0, 6): # 1, 2, 3, 4, 5
    for j in range(5, i, -1): # 5, 4, 3, 2
        z += str(j) + ' '
    z += '\n'
print(z)
print()

# Lat 7:
#              * 
#           *  *  * 
#        *  *  *  *  * 
#     *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  * 
#     *  *  *  *  *  *  * 
#        *  *  *  *  * 
#           *  *  * 
#              * 

print("Latihan 7:")
z = ''
for i in range(0, 6): # 0, 1, 2, 3, 4, 5
    for j in range(0, 5 - i): # 0, 1, 2, 3, 4
        z += '   '
    for k in range(1, 2 * i): # 1, 
        z += ' * '
    z += '\n'
for a in range(0, 5):
    for c in range(0, a):
        z += '   '
    for b in range(1, (5 * 2) - 2 * a):
        z += ' * '
    z += '\n'
print(z)

for i in range(1, 6):
    print('  '  * (6 - i) + (str(i) + ' ') * i)

# z = ''
# temp = ''
# for i in range(0, 3):
#     for j in range(0, i+1):
#         z += str(i) + ' '
#         temp += 'nilai i %d nilai j ke-%d\n' %(i, j)
#     z += '\n'
# print(z)
# print(temp)