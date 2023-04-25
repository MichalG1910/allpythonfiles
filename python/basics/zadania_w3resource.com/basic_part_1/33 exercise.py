# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
# Napisz program w języku Python, aby zsumować trzy podane liczby całkowite. Jeśli jednak dwie wartości są równe, suma będzie równa zero

def sum(a,b,c):
    if a == b or b == c or c == a:
        print(0)

    else:
        print(f"a + b + c = {a + b + c}")

sum(3,5,7)
sum(3,9,3)
