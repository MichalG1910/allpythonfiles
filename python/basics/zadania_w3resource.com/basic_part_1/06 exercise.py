# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

a = input("podaj sekwencję cyfr po przecinku: ")      # nie do końca działa!!!!
list1 = list(a)
list2 = []
for v in list1:
    if v != ",":
        list2.append(v)

print("List :", list2)
print("Tuple :", tuple(list2))


# rozwiązanie z strony (użycie split)
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)