#!/usr/bin/python3

# Zmienne

one_line_string = "To jest string w jednej lini."

multi_line_string = """
To jest string ktory
jest w wiecej
niz jednej lini

moze zawierac spacje
        takze wciecia za pomoca tabulacji
  lub spacji
"""
user = "PiotrKoska"

#print("%s" % (one_line_string))
#print("%s" % (multi_line_string))

#print("-------------------------")

#print("{} to pierwsza zmienna. {} tu druga zmienna".format(one_line_string, multi_line_string))

#print(f"{one_line_string} to pierwsza zmienna. {multi_line_string} tu druga zmienna")

pozycja_litery = multi_line_string.find('a')

#print("Pozycja {}".format(pozycja_litery))

#print("59 Pozycja to: {}".format(multi_line_string[59]))

#print("Zmienna multi_line_string jest: {}".format(type(multi_line_string)))

#print("Nazwa Uzytkownika w systemie Linux: {} ".format(user.lower()))

print("Rozdzielone\tTabem")
print("To pierwsza linia\nTo druga linia")
