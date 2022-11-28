# Write a Python program to concatenate all elements in a list into a string and return it

list = [1,4,5,7,9,0,12]
string = "liczba"

for v in list:
    i = str(v) + string
    print(i)
# źle zrozumiałem z angielskiego


# rozwiązanie w3resource
def concatenate_to_string(list):
    start = ""
    for i in list:
        start += str(i)
    return start

print(concatenate_to_string([1,4,5,7,9,0,12]))