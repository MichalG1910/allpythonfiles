
'''
Klasa Cursor biblioteki psycopg zapewnia metody wykonywania poleceń PostgreSQL w bazie danych przy użyciu kodu Pythona.
Korzystając z jego metod można wykonywać instrukcje SQL, pobierać dane z zestawów wyników, wywoływać procedury.
Możesz utworzyć obiekt Cursor za pomocą metody kursor() obiektu/klasy Connection.


Metody
Poniżej przedstawiono różne metody udostępniane przez klasę/obiekt klasy Cursor:

callproc()      - Ta metoda służy do wywoływania istniejących procedur bazy danych PostgreSQL.	
close()         - Ta metoda służy do zamykania bieżącego obiektu kursora.	
executemany()   - Ta metoda akceptuje serię list parametrów listy. Przygotowuje zapytanie MySQL i wykonuje je ze wszystkimi parametrami.	
execute()       - Ta metoda przyjmuje zapytanie MySQL jako parametr i wykonuje podane zapytanie.	
fetchall()      - Ta metoda pobiera wszystkie wiersze w zestawie wyników zapytania i zwraca je jako listę krotek. (Jeśli wykonamy to po pobraniu kilku wierszy, zwróci pozostałe)	
fetchone()      - Ta metoda pobiera następny wiersz w wyniku zapytania i zwraca go jako krotkę.	
fetchmany()     - Ta metoda jest podobna do metody fetchone(), ale zamiast pojedynczego wiersza pobiera następny zestaw wierszy w zestawie wyników zapytania.


Poniżej przedstawiono właściwości klasy Cursor:
	
dscription      - Jest to właściwość tylko do odczytu, która zwraca listę zawierającą opis kolumn w zestawie wyników.
astrowid        - Jest to właściwość tylko do odczytu, jeśli w tabeli znajdują się kolumny z autoinkrementacją, zwracana jest wartość wygenerowana dla tej kolumny w ostatniej operacji INSERT lub UPDATE.
rowcount        - Zwraca liczbę wierszy zwróconych/zaktualizowanych w przypadku operacji SELECT i UPDATE.	
closed          - Ta właściwość określa, czy kursor jest zamknięty, czy nie, jeśli tak, zwraca wartość true, w przeciwnym razie zwraca wartość false.
connection      - Zwraca to odwołanie do obiektu połączenia, za pomocą którego utworzono ten kursor.	
name            - Ta właściwość zwraca nazwę kursora.	
scrollable      - Ta właściwość określa, czy dany kursor można przewijać.
'''