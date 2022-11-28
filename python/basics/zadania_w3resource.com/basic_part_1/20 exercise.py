# Write a Python program to get a string which is n (non-negative integer) copies of a given string. 

str = input("Podaj wyraz: ")
copyNum = int(input("Podaj liczbę kopii: "))

def string_copys(string, number):
    result = (string + " ") * number
    return result

print(string_copys(str, copyNum))


# rozwiązanie ze strony w3resource    
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))
