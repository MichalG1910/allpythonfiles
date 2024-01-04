# Write a Python program to compute the greatest common divisor (GCD) of two positive integers. GCD- największy wspólny dzielnik
from math import gcd

a = 336
b = 360
a1 = a
b1 = b
listA = []
listAA = []
listB = []
listBB = []


while True:
    listA = list(range(2,a +1))
    for i in listA:
        if a % i != 0:
            continue
        if a % i == 0:
            listAA.append(i)
        break
    a = int(a / i)
    if listA == []:
        break

print("listAA: ", listAA)

while True:
    listB = list(range(2,b +1))
    for i in listB:
        if b % i != 0:
            continue
        if b % i == 0:
            listBB.append(i)
        break
    b = int(b / i)
    if listB == []:
        break

print("listBB: ", listBB)
listFinall = []
for v in listAA:
    if v in listBB:
        listFinall.append(v)
        listBB.remove(v)

print("listFinall: ", listFinall)
greatest_common_divisor = 1
for v in listFinall:
    greatest_common_divisor = greatest_common_divisor * v

print(f"GCD największy wspólny dzielnik {a1} i {b1} = {greatest_common_divisor}")


print("\n-----------------------------2--------------------------------------\n")
# jest taka funkcja w bibliotece math
x = 336
y = 360
print(gcd(x, y), "\n")

print("\n-----------------------------3--------------------------------------\n")

# rozwiązanie w3resource
def gcd1(x, y):
   gcd1 = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1): # [8, 7, 6, 5, 4, 3, 2, 1]
       if x % k == 0 and y % k == 0:
           gcd1 = k
           break 
   return gcd1
print("GCD of 12 & 17 =",gcd1(12, 17))
print("GCD of 4 & 6 =",gcd1(4, 6))
print("GCD of 336 & 360 =",gcd1(336, 360))
