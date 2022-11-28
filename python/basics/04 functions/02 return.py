
def addNumbers(a,b,c): 
    return a + b + c    # zwrócona zostanie suma parametrów zdefiniowanej przez nzs funkcji (a,b,c - parametry)

print(addNumbers(123,234,345))  # 702, (123,234,345)- argumenty- dane które podstawimy do funcji, aby ją wykonać

print(' ')

def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista!!!")
        return None
    result = 0          # cały ten zapis
    for v in listData:  # powoduje, że zostanie zliczona 
        result += v     # suma wszystkich elementów listy
    return result       # i zwrócony zostanie wynik

print(sumListElements([])) # Pusta lista!!!
print(sumListElements([1,2,3,4,5,6,7,8,9,])) # 45

print(' ')


def printList(listData):
    if len(listData) == 0:
        return              # funkcja return powoduje zakończenie pętli, jeśl spelniony jest warunek
                            # w tym przypadku nie zostanie zwrócony żaden wynik ( pusta lista )
    for v in listData:
        print(v)
    return  # jeśli nie oczekujemy jakiejś konkretnej akcji, funkcja return może zostać pominięta,
            # w tym przypadku zostaną zwrócone parametry listy (innej niż pusta lista)

printList([])   # w przypadku pustej listy nie zostanie wyświetlony żaden wynik
printList([6,7,8])

