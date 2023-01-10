
# property - własności
# getter, setter - ustawiacz, pobieracz

class KontoBankowe:
    __stan = 0

    @property               # tworzenie właściwości. definicja przestaje pełnić rolę funkcji 
    def stan_konta(self):   # a jest traktowana prawie jak zwykła zmienna (ale jest tylko do odczytu)
        return self.__stan  # jeśli byśmy spróbowali ją wywołać i nadać jej inną wartość (konto.stan_konta = 50) - błąd
                            # będzie to możliwe dopiero po użyciu gettera i settera

    @stan_konta.getter      # tworzenie gettera dla @property - da nam to możliwość ustawienia nowego np. zapisu we właściwości 
    def stan_konta(self):
        return "stan konta: " + str(self.__stan) + "zł"

    @stan_konta.setter           # tworzenie settera dla @property - da nam to możliwość w trakcie wywołania pobrać inną wartość
    def stan_konta(self, value): # w tym przypadku (self.__stan += value) zwiększymy stan naszego konta o argument value
        self.__stan += value

konto = KontoBankowe()
print(konto.stan_konta) # stan konta: 0zł - korzystając z @property def stan_konta nie użuwamy (), 
# bez @property - print(konto.stan_konta()) - jakbyśmy próbowali to tak wywołać, spowoduje to błąd

konto.stan_konta = 50 # stan konta: 50zł  - (+50)
print(konto.stan_konta)
konto.stan_konta = 100 # stan konta: 150zł  - (+100)
print(konto.stan_konta)
konto.stan_konta = -125 # stan konta: 25zł  - (-125)
print(konto.stan_konta)
