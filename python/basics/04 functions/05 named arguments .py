# named arguments - nazwane argumenty. Domyślnie wpisując argumenty do wywołania naszej funkcji wpisujemy tylko 
# parametr pamietając o tym, żeby kolejność ich wpisywania była taka sama jek w definicji naszej funkcji. 
# Możemy przy wywoływaniu naszej funkcji skorzystać zarówno z nazwy argumentu, jak i z parametru, jaki do niego
# przypiszemy(np: brand = "Ford"). Taki zapis pozwala nam obejść konieczność wpisywania po kolei parametrów

def printCar(brand, name = "concept", year = 1960, color = "black"):
    print(brand, name, year, color)

printCar(name = "T", brand = "Ford") # wynik: Ford T 1960 black
printCar(year = 1920, name = "T", brand = "Ford") # wynik: Ford T 1920 black

# zwróć uwagę, że python automatycznie ustawi kolejność wyświetlanych danych w takim przypadku (jak w definicji funkcji)