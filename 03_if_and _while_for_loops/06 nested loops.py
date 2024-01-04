# nested loops - pętle zagnieżdżone

listsData = [
    [0,1,2,3,4,],
    [ "Ala", "Ola", "Adam"],            # lista kilku list
    [10, "Adam", 20, "Ania"]
]

for listData in listsData: # iteracja każdej listy ze zmiennej listsData
    for v in listData:
        print(v, end=' ')
        
