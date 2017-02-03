import math
a = 1
b = 1
c = 0
count = 2
while int(math.log10(a))+1 < 1000:
    c = a
    a += b
    b = c
    count += 1

print(count)
