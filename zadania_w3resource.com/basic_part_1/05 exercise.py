# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

name = input("podaj imię i nazwisko: ")
list1 = []
str1 = len(name)
for i in name:
    v = str(i) 
    list1.append(v)
    
list1.reverse()
print(" ".join(list1))