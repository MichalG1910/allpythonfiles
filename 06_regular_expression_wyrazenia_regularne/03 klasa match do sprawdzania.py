
import re
class Match:
    
    def rematch(self, wzor, tekst):
        self.wzor = wzor
        self.tekst = tekst

        if re.match(wzor, tekst):                              
            print("Dopasowano!")
        else:
            print("Nie dopasowano!")
    
w1 = Match()

print("|1|---------------------------------------")
w1.rematch("ko.", "kot")  # Dopasowano!  
w1.rematch("ko.", "koc")  # Dopasowano!  
w1.rematch("ko.", "ko$")  # Dopasowano!  
w1.rematch("ko.", "ko9")  # Dopasowano!  
w1.rematch("ko.", "ko ")  # Dopasowano!  

print("|2|---------------------------------------")
w1.rematch("^ko.$", "kotttt")  # Nie dopasowano!
w1.rematch("^ko.$", "kot")  # Dopasowano!

print("|3|---------------------------------------")
w1.rematch("^[Kk]o.$", "lot")  # Nie dopasowano!
w1.rematch("^[LlKk]o.$", "lot")  # Dopasowano!
w1.rematch("^[LlKk]o.$", "Lot")  # Dopasowano!
w1.rematch("^[LlKkp]o.$", "pot")  # Dopasowano!
w1.rematch("^[a-z]o.$", "pot")  # Dopasowano!
w1.rematch("^[A-Z]o.$", "pot")  # Nie dopasowano!
w1.rematch("^[A-Za-z]o.$", "pot")  # Dopasowano!
w1.rematch("^[A-Za-z]o.$", "Pot")  # Dopasowano!
w1.rematch("^[^A-Za-z]o.$", "Pot")  # Nie dopasowano!
w1.rematch("^[^A-Ka-k]o.$", "Pot")  # Dopasowano!
w1.rematch("^[^A-Za-z]o.$", "$ot")  # Dopasowano!

print("|4|---------------------------------------")
w1.rematch("^[Rr]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok-1984")  # Dopasowano!
w1.rematch("^[Rr]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok-984")  # Nie dopasowano!
w1.rematch("^[Rr]ok[-_=][0-9]*$", "Rok_984")  # Dopasowano!
w1.rematch("^[Rr]ok[-_=][0-9]*$", "rok_145634984")  # Dopasowano!
w1.rematch("^[Rr]ok[-_=][0-9]*$", "rok_")  # Dopasowano!

print("|5|---------------------------------------")
w1.rematch("^[A-Z][a-z]a*$", "Al")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]a*$", "Ala") # Dopasowano!  
w1.rematch("^[A-Z][a-z]a*$", "Alaaa") # Dopasowano!   
w1.rematch("^[A-Z][a-z]a*$", "Alc") # Nie dopasowano!  
w1.rematch("^[A-Z][a-z]a*$", "Alan") # Nie dopasowano!    
w1.rematch("^[A-Z][a-z]a*$", "al") # Nie dopasowano! 

print("|6|---------------------------------------")
w1.rematch("^[A-Z][a-z]a+$", "Ala")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]a+$", "Alaaaa")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]a+$", "Al")  # Nie dopasowano! 

print("|7|---------------------------------------")
w1.rematch("^[A-Z][a-z]?[A-Z]$", "AA")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]?[A-Z]$", "AdA")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]?[A-Z]$", "AddA")  # Nie dopasowano!  

print("|8|---------------------------------------")
w1.rematch("^[A-Z][a-z]{2,5}$", "Ala")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]{2,5}$", "Alabcd")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]{2,5}$", "Al")  # Nie dopasowano!  
w1.rematch("^[A-Z][a-z]{2,}$", "Sebastian")  # Dopasowano!  
w1.rematch("^[A-Z][a-z]{,5}$", "Sebastian")  # Nie dopasowano!  
w1.rematch("^[A-Z][a-z]{,5}$", "A")  # Dopasowano!  

  

    
    
    
    
    
    
    