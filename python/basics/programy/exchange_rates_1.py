import datetime
import requests # import biblioteki requests niezbędnej do pobrania danych z serwera
# jeśli python nie widzi jakiejś biblioteki, trzeba ją zainstalować w terminalu:
# pip install requests
plik = open("./allpythonfiles/python/basics/programy/raport exchangerates.txt", "w") 

if plik.writable():
     
    data1 = input('podaj datę początkową(RRRR-MM-DD):')
    data2 = input('podaj datę końcową(RRRR-MM-DD):')
    plik.write(f"podaj datę początkową(RRRR-MM-DD): {data1}\n")
    plik.write(f"podaj datę końcową(RRRR-MM-DD): {data2}\n\n")
    if data1 == '' and data2 == '':
        response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
        print('ilośc sprawdzanych dni: ', 1)
        plik.write('ilość sprawdzanych dni: 1\n')
        daysLen = 1
    else:   
        response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{data1}/{data2}/?format=json")

        data1_list = (list(data1.split('-')))
        sdList = [int(i) for i in data1_list] # to samo co niżej, tylko uproszczone
        '''
        for i in data1_list:
            sdList.append(int(i))
        '''
        data2_list = (list(data2.split('-')))
        edList = [int(i) for i in data2_list]
        startDate = datetime.date(sdList[0], sdList[1], sdList[2])
        endDate = datetime.date(edList[0], edList[1], edList[2])
        days = endDate - startDate
        daysLen = days.days
        print('ilośc sprawdzanych dni: ', daysLen)
        plik.write(f'ilośc sprawdzanych dni: {daysLen}\n')

    if response.ok == True: # sprawdzenie, czy serwer odpowiada poprawnie
        data = response.json()[0:daysLen] # parsowanie danych z formatu teksowego na format do odczytu w python
        print('ilość raportów NBP z tych dni (tylko dni pracujące):', len(data)) # wynik jest to lista która zawiera słownik. W tym słowniku mamy klucz "rates" którego wartość 
        plik.write(f'ilość raportów NBP z tych dni (tylko dni pracujące): {len(data)}\n\n')
        # zawiera następną listę słowników, już z danymi nas interesującymi, czyli kursami walut
        
            
        for dict in data:
            table = dict["table"]
            no = dict["no"]
            effectiveDate= dict["effectiveDate"]
            print("\nExchange rates: ", table, no, effectiveDate)
            plik.writelines(f"Exchange rates: {table}, {no}, {effectiveDate}\n")
            rates = dict["rates"]
            for rate in rates:
                currency = rate["currency"]
                code = rate["code"]
                mid = rate["mid"]
                print(currency, "code: ", code, "value: ", mid)
                plik.write(f"{currency}, code: {code}, value: {mid}\n")
            print('ilość walut: ',len(rates))
            plik.write(f"ilość walut: {len(rates)}\n\n")
plik.close()


