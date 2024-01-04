num = 0
operations = None
reset = True
result = None
calcOperatins = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("podaj pierwszą liczbę: "))
        reset = False# musimy wprowadzić False ponieważ po wykonaniu jednego obliczenia kalkulator by sie resetował
    
    operations = input( "Podaj operację arytmetyczną " + str(calcOperatins) + " lub exit jeśli koniec lub reset: ")
    if operations == "exit": break
    if operations == "reset":
        reset = True
        continue
    
    if not operations in calcOperatins:
        print(" Wprowadzona operacja jest błędna!")
        continue

    secondNum = int(input("Podaj drugą liczbę: "))
    
    if operations == "+":
        result = num + secondNum
    
    if operations == "-":
        result = num - secondNum
    
    if operations == "*":
        result = num * secondNum
    
    if operations == "/":
        result = num / secondNum
    
    if operations == "**":
        result = num ** secondNum

    print( "Wynik operacji" + " " + str(num) + " " + operations + " " + str(secondNum) + " = " + str(result))
    num = result
    result = None # ten zapis spowoduje, że kiedy ponownie progran zacznie wykonywać pętlę while, to wartość
    # początkowa dla której będziemy wykonywać kolejne działanie arytmetyczne = naszemu rezultatowi z poprzedniej pętli
    




