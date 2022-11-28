from tkinter.messagebox import YES


shopShelf = ["Banana", "Orange", "Peach", "Kiwi", "Apple", "Mushrooms"]
basket = []

goods = len(shopShelf)

print("Shop Shelf:" )
for product in shopShelf:
    print(product, end = ", ")

watchingGoods = 0
while watchingGoods < goods:
    print("\nYou have a {}".format(shopShelf[watchingGoods]))
    choice = input("Put theme into Your basket?")
    if choice == YES:
        basket.append(shopShelf[watchingGoods]) # dodanie do basket musi być pierwsze przed usunięciem z shopshelf
        shopShelf[watchingGoods] = ""
       
    watchingGoods += 1
  
print("\nInto a Shop Shelf:" ) 
for product in shopShelf:
    print(product, end = ", ")
    
print("\nInto Your basket:")   
for inBasket in basket:
    print(inBasket, end = ", ")