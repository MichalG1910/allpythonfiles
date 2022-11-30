class Car:
    def __init__(self,model,brand,vinnumber):
        self.model = model
        self.brand = brand
        self.vinnumber = vinnumber

    def printInformation(self):
        print("My Model is: ", self.model)
        print("My Car Brand is: ", self.brand)
        print("My Car has vin number: ", self.vinnumber)

myCar1 = Car("126p","Fiat","Gh6756hGHgghj87656")
myCar2 = Car("125p","Fiat","GHTH66756535463655")

myCar1.printInformation()
print('')
myCar2.printInformation()

