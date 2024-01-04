# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
# Napisz program w języku Python, który zwróci wartość true, jeśli dwie podane wartości całkowite są równe lub ich suma lub różnica wynosi 5

def sum(a, b):
    if a == b or a + b == 5 or a - b == 5 or b - a == 5:
        return print(True)
    else:
        return print(False)

sum(5, 5)
sum(10, 20) 
sum(10, 5) 
sum(10, -5) 
sum(2, 3)
print()
sum(7, 2)
sum(3, 2)
sum(2, 2)
sum(7, 3)
sum(27, 53)