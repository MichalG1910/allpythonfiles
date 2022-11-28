
# Write a Python program to test whether a passed letter is a vowel or not. vowel - samogłoska

vowel = ("a", "ą", "e", "ę", "i", "o", "u", "y")
def isSheVowel(n):
    if n in vowel:
        return str(n) + " jest samogłoską"
    else:
        return str(n) + " nie jest samogłoską"

print(isSheVowel("z"))
print(isSheVowel("a"))

# rozwiązanie z w3resource

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))