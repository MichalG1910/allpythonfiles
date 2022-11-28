
data = [0,1,2,3,4,5,6]
for i in data:          # wynik działania [0,2,4] =  iteracja listy data zostanie przerwana, jeśli 
    if i == 3:          # wartość zmiennej i będzie równa 3 (zakończy ją funkcja break)
        break
    print( i * 2 )

print("")

for i in data:              # jęśli i=3 albo i=5, pętla for będzie dziaałała, jednak wartość 3 oraz 5 
    if i == 3 or i == 5:    # zostaną pominiet i nie zostaną wyświetlone (odpowiada za to funkcja continue)
        continue            # wynik: [0,1,2,4,6,]
    print(i)

print("")

if 10 > 2:
    pass        # funkcja pass to taki wypełniacz, który nic nie znaczy. Używamy go wtedy, 
else:           # kiedy jakaś instrukcja wymaga dalszego kodu aby nie wygenerować błędu, jednak my nie chcemy 
    pass        # go tam wstawiać. W przyszłości możemy usunąć pass i zastąpić go docelowym kodem