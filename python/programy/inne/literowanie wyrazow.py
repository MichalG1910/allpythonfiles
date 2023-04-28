# taki mały program do literowania

while True:
    number = 1
    print( "wprowadź wyraz do przeliterowania lub exit by wyjść: ")
    wyraz = input()
    if wyraz == "exit" : break
    liczbaZnaków = len(wyraz)
    while number < liczbaZnaków:
        for v in wyraz:  
            print( str(number)+ ". " + v)
            number += 1
        
# nawet działa jak należy