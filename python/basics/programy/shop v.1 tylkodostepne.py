
from tkinter.messagebox import YES

startShopShelf = ("Banana", "Orange", "Peach", "Kiwi", "Apple", "Mushrooms")
shopShelf = list(startShopShelf)
basket = []

goods = len(shopShelf)

print("Shop Shelf:" )
for product in shopShelf:
    print(product, end = ", ")

watchingGoods = 0
while watchingGoods < goods:
    print("\nYou have a {}".format(startShopShelf[watchingGoods]))
    choice = input("Put theme into Your basket?")
    if choice == YES:
        basket.append(startShopShelf[watchingGoods])
        shopShelf.remove(startShopShelf[watchingGoods])

    watchingGoods += 1
       
print("\nInto a Shop Shelf:" ) 
for product in shopShelf:
    print(product, end = ", ")
    
print("\nInto Your basket:")   
for inBasket in basket:
    print(inBasket, end = ", ")

    


    

