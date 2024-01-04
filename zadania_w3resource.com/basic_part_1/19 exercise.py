# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.


def string_new(string):
    if string[0] == "i" and string[1] == "s": 
        return string
    else:
        return "is" + string
print(string_new("Array"))
print(string_new("isEmpty"))

# rozwiązanie ze strony w3resource

def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))