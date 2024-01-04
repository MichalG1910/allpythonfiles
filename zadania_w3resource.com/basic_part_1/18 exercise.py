# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

n1 = int(input("Podaj pierwszą liczbę: "))
n2 = int(input("Podaj drugą liczbę: "))
n3 = int(input("Podaj trzecią liczbę: "))
if n1 == n2 == n3: print(str((n1+n2+n3) * 3)) 
else:
    print(n1+n2+n3)

# rozwiązanie z w3resource
print(" ")
def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))