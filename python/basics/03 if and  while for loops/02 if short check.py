
# sprawdzenie instrukcji if dla typu boolean(logiczny)

# 3 sposoby sprawdzenia True, preferowany zapis skrócony (ostatni) 
flag = True
if flag == True:
    print( "flag równe jest True" )

if flag is True:
    print( "flag is True" )

if flag:
    print( "flag równe jest True" )

# 3 sposoby sprawdzenia False, preferowany zapis skrócony (ostatni)
flag1 = False
if flag1 != True:
    print( "flag1 równe jest False" )

if flag1 == False:
    print( "flag1 równe jest False" )

if flag1 is not True:
    print( "flag1 is False" )

if not flag1:
    print( "flag1 równe jest False" )



