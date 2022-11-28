
number = 10                # typ wartości <class 'int'>  integer- liczba całkowita
print(number) 
print(type(number))

info = "hello"             # typ wartości <class 'str'>  string-łańcuch znaków
print(info)
print(type(info))

x = 3.14                   #<class 'float'>   liczba zmiennoprzecinkowa tzw float to liczba rzeczywista,
print(x)                   #czyli ma część calkowitą i ułamkową po kropce
print(type(x))  

complexNum = 10 + 3j       #<class 'complex'> liczba zespolona będąca sumączęści rzeczywistej i urojonej
print(complexNum)          #obie przechowywane jako liczby float
print(type(complexNum))    

a = 1
b = 4.5

print(isinstance(a, int)) # True, sprawdza, czy dana zmienna ma konkretny typ
print(isinstance(b, float)) # True

# w python wszystko jest obiektem. Zmienna a jest obiektem klasy int(integer). Jeśli użyjemy funkcji dir,
# to jako wynik otrzymamy wszystkie metody dostępne dla tego obiektu klasy int (to samo dotyczy funkcji)

print(dir(a)) # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
#'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__',
#  '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', 
# '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__',
#  '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
#  '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
#  '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
#  '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
#  '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
#  'imag', 'numerator', 'real', 'to_bytes']
 