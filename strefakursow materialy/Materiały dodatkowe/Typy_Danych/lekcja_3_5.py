#!/usr/bin/python3

# Tuples

point = (10.0, 40.0, 50) # Tuple
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_string = "Tutaj mój dowolny string"

# Rożnice

#print("Adres w pamieci tuple: {}".format(id(point)))
#print("Adres w pamieci listy: {} <------".format(id(my_list)))
#print("Adres w pamieci string: {}".format(id(my_string)))

#point = point + (10, 20)
#my_list[2:5] = ["A", "B", "C", "D", "E", "F"]
#my_string += " dowolny dodany string"

#print("--------------------------------------------")
#print("Adres w pamieci tuple: {}".format(id(point)))
#print("Adres w pamieci listy: {} <-----".format(id(my_list)))
#print("Adres w pamieci string: {}".format(id(my_string)))

x, y, z = point

print("x:{},y:{},z:{}".format(x, y, z))
print("Wspolrzedne: x: %s y: %s z: %s" % point)
