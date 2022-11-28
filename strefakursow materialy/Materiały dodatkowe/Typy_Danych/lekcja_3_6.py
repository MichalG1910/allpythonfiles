
#dicts

ages = dict([('piotr',30), ('adam',40), ('karolina',50)])

#print("Piotr ma: {} lat".format(ages['piotr']))
print("Slownik: {} typu {}".format(ages,type(ages)))
ages['roman'] = 19
ages['natalia'] = 20
print(ages)
ages['karolina'] = 30
print(ages)
#print(ages['monika'])
#del ages['karolina']
#print(ages)
#del ages
#print(ages)
#ages.pop()
#print(ages)
print(ages.keys())

lista_imion = list(ages.keys())

print("Na liście mamy: {} jest to typ {}".format(lista_imion,type(lista_imion)))

print(ages.values())
