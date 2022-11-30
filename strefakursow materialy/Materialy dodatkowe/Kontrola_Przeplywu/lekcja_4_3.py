
# while

count = 0

while count <= 100:
    if count % 50 == 0:
        count +=1
        continue
    if count % 20 == 0:
        break
    print("Liczby nie parzyste: {}".format(count))
    count += 1

print("Koniec pętli")
