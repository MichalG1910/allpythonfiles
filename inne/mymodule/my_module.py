x = 1
def my_function(name = "Zenon"):
    return "Odczyt z modułu my_module: \nWitaj " + name

if __name__ == "__main__": 
    print("Script run as main script")
else:
    print("Script - import as module")
# Zapis powyżej powoduje rozpoznanie, czy nasz skrypt my_module:
    # został  uruchomiony z poziomu skryptu - otrzymamy: Script run as main script
    # został zaimportowany do innego skryptu i tam uruchomiony jako moduł: Script - import as module

