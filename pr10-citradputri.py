# Berapa jumlah total dari bilangan ganjil yang telah 
# dipangkat 3 dari 1 - 200

from functools import reduce
total = reduce(lambda x, y: x + y, list(map(lambda x: x ** 3, list(filter(lambda x: x % 2 != 0, range(1, 201))))))
print(total)
