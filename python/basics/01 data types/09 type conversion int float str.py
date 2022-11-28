
floatNum = 23.9999
intNum = int(floatNum) # konwersja typu zmiennej z float(rzeczywista) na int(całkowita)
print(intNum)
print(type(intNum))

print(int("654   ")) # przykłady konwersji na typ int (liczba całkowita)
print(int(99))

intNum = 56
float1 = (float(intNum)) # konwersja z int(calkowita) na float(rzeczywista)
print(type(float1))
print(float1)

str1 = "123.3467987767"
float2 = float(str1) # konwersja z str(łańcuch znakóww) na float (rzeczywista)
print(type(float2))
print(float2)
print(float(35.5665))

# aby łączyć z łańcuchem znaków inne typy zmiennych musimy koniecznie przekonwertować je na typ str (łańcych znaków) 
print("wartość float1: " + str(float1) + " " + str(96.1910) + " " + str([1,2,3,4]))
# podobny wynik otrzymamy używając znaku specjalnego w funkcji print "," (przecinek)
print("wartość float1: ", float1, " " , 96.1910, [1,2,3,4])


 

