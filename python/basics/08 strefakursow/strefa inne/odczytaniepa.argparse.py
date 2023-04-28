import time, os, sys, argparse

# pathFrom = sys.argv[1] # ten moduł powoduje, że uruchamiając skrypt musimy się odnieść do pliku który ma być stworzony
# z naszymi parametrami, lub jeśli jest utworzony, to wyświelti nasze parametry
# PS D:\python> & "c:/Users/mgrabarz3/Desktop/Portable Python-3.7.9/App/Python/python.exe" d:/python/basics/programy/odczytanieparametrowserwera.py "./servermich.conf"

def readFromFile(*path_to_file):
    if path_to_file is not None:
        for path in path_to_file:
            serverFile = open(path, "r")
            serverConfiguration = serverFile.read() # def otwarcia pliku do odczytu 
        print(serverConfiguration)
        serverFile.close()

def writeToFile(*path_to_files):
    if path_to_files is not None:
        for path in  path_to_files:
            serverFile = open(path, 'w')  # def zapisania zmian w pliku
            title = "DEVELOPER MODE\n"
            serverFile.write(title)
            serverParams = [ "CPU=20\n", "RAM=30G\n", "TOTALDISK=3\n", "\t/dev/sda, /dev/sdb, /dev/sdc\n", "GPURAM=6G\n"  ]
            serverFile.write(''.join(serverParams))
        serverFile.close()

def main(): #
    parser = argparse.ArgumentParser() #
    parser.add_argument("-f", "--file", action = "store", dest = "pathFrom", default = "./servermich.conf", help = "Path to your file") #

    result = parser.parse_args() # te linie powodują, że uruchamiając skrypt bezpośrednio nie otrzymamy błędu

    startTime = time.localtime()
    print("Script start time: {}:{}:{}".format(startTime.tm_hour, startTime.tm_min, startTime.tm_sec ))

    stage = os.getenv("STAGE", default = "dev").upper()

    if stage.startswith("PROD"): # sprawdzamy, czy server jest produkcyjny, jeśli tak, to przerywamy skrypt
        output = f"SERVER is in {stage} mode"
        print(output)
        exit()
    elif os.path.exists(result.pathFrom): # sprawdzamy, czy plik istnieje, jeśli tak to odczytujemy go
        readFromFile(result.pathFrom) # mamy tu zmianę i odwołanie do def main()
    else:
        writeToFile(result.pathFrom) # zapisujemy plik (jeśli nie istnieje, to zostanie utworzony)

    stopTime = time.localtime()
    difference = time.mktime(stopTime) - time.mktime(startTime)
    print("Script stop time: {}".format(time.strftime("%X", stopTime)))
    print("Total Script work: {}".format(difference))

if __name__ == "__main__":
    main()


# "rm" w terminalu usuwa plik np. rm servermich.conf usunie plik servermich.confls
# "ls" - pokaże nam pliki w katalogu, z którego wywołamy
# " cd" - wejście do katalogu np. cd basics