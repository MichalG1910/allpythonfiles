from klasa11polagettery_settery import Example

obiekt = Example()
print(obiekt.get_example_field()) # 10

obiekt.set_example_field(50)
print(obiekt.get_example_field()) # 50

obiekt.example_field = -40 # if value_field < 0: self.__example_field = 0
print(obiekt.get_example_field()) # 0

obiekt.set_example_field(-6050) # 
print(obiekt.get_example_field()) # 0



