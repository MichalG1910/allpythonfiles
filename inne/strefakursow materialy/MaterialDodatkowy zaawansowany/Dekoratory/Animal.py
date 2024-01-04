class Animal:
    howManyAnimal = 0

    @classmethod
    def __init__(cls,self,name_animal):
        self.name_animal = name_animal
        cls.howManyAnimal += 1