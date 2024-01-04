
import re

print("|1|")
if re.match("ko.", "kot"): # kropka zastępuje każdy znak, więc konsola wyświetli, że arg1 dopasowano do arg2
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

print("|2|")
if re.match("^ko.$", "kotttt"): # ^ -pokazuje, gdzie ma się zaczynać dany wzór, $ - gdzie ma się kończyć
    print("Dopasowano!")        # Nie dopasowano! - przeszukiwany tekst nie kończy się jak we wzorze
else:                           # aby dopasowało, drugi argument musiałby wyglądać tak: "kot"
    print("Nie dopasowano!")


print("|3|")
if re.match("^[Kk]o.$", "lot"): # [Kk] lub [pk] - tzw. klasa znaku - będzie szukało w tekśccie liter 
    print("Dopasowano!")        # z nawiasu[]. Jeśli jakaś z nich będzie w naszym tekście, to: Dopasowano!
else:                           # Nie dopasowano
    print("Nie dopasowano!")


print("|4|")
if re.match("^[Rr]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok-1984"): # Dopasowano  
    print("Dopasowano!")        
else:                            
    print("Nie dopasowano!")


print("|5|")
if re.match("^[A-Z][a-z]a*$", "Alaaa"): # * - gwiazdka stojąca za znakiem/klasą znaków/literą dopuszcza wystąpienie 
                                     # jej nieskończoną ilość razy lub niewystąpienie jej wcale
    print("Dpoasowano!")
else:
    print("Nie dopasowano!")

print("|6|")
if re.match("^[A-Z][a-z]a+$", "Al"): # plus działa podobnie jak gwiazdka z tą różnicą, że znkak za którym stoi 
                                     # musi wystąpić conajmniej 1 raz(może nieskończoną ilość razy)
    print("Dpoasowano!")             # Nie dopasowano!
else:
    print("Nie dopasowano!")

print("|7|")
if re.match("^[A-Z][a-z]?[A-Z]$", "AA"): # ? - znak, za którym stoi może nie wystąpić wcale lub wystąpić 1 raz
    print("Dpoasowano!")             # Dopasowano!
else:
    print("Nie dopasowano!")

print("|8|")
if re.match("^[A-Z][a-z]{2,5}$", "Ala"): # {2,5} - znak, za którym stoi może wystąpić od 2 do 5 razy
    print("Dpoasowano!")             # Dopasowano!
else:
    print("Nie dopasowano!")





# re.match(wzór do szukania, tekst do przeszukania)
# ^ -pokazuje, gdzie ma się zaczynać dany wzór
# $ - gdzie ma się kończyć dany wzór
# ko. - kropka zastępuje każdą literę, wyrazy np. kot, koc, koń będą dopasowane poprawnie
# [Kk] - szuka w tekście liter Wielkie i małe K
# [A-Z] - szuka w tekście liter z przedziału A-Z (wielkie litery)
# [A-Za-z] - szuka w tekście liter z przedziału A-Z (wielkie i małe litery)
# [^A-Ca-c] - ^ - zastosowanie w klasie znaku ^ powoduję negację danego zakresu liter. W tym 
#           przypadku będzie szukało w tekście wszystkich liter z poza zakresu małych i wielkich A-C 
# [A-Z][a-z]a* - * - gwiazdka stojąca za znakiem/klasą znaków/literą dopuszcza wystąpienie 
#                    jej nieskończoną ilość razy lub niewystąpienie jej wcale          
# [A-Z][a-z]a+ - + - plus działa podobnie jak gwiazdka z tą różnicą, że znkak za którym stoi musi wystąpić 
#                    conajmniej 1 raz(może nieskończoną ilość razy)  
# ^[A-Z][a-z]?[A-Z]$ - ? - znak, za którym stoi może nie wystąpić wcale lub wystąpić 1 raz 
# ^[A-Z][a-z]{2,5}$ - znak, za którym stoi może wystąpić od 2 do 5 razy     
# ^[A-Z][a-z]{2,}$ - znak, za którym stoi może wystąpić od 2 nieskończonej ilości razy     
# ^[A-Z][a-z]{,5}$ - znak, za którym stoi może wystąpić od 0 do 5 razy     