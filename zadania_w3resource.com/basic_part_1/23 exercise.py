
# Write a Python program to get the n (non-negative integer - nieujemną całkowitą) copies of the first 2 
# characters of a given string. Return the n copies of the whole string if the length is less than 2.

def copys(string, nCopys):
    str = len(string)
    if str > 2:
        return (string[0:2] + " ")  * nCopys
    else:
        return (string + " ")  * nCopys
print(copys("Wyimaginowany", 7))
print(copys("I", 12))

print()

# rozwiązanie z w3 resource
def substring_copy(str, n):
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))