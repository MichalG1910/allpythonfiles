#!/usr/bin/python3

# Lista w python

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

my_list2 = [ "slowo", "a"," s d d", 3, 5 ]

# String 'str' object does not support item assignment.!
#my_string[0] = "C"

my_list.append('D')
my_list.append("F")

print(my_list)

my_list += my_list2

print(my_list)


