# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

colorList1 = set(["White", "Black", "Red"])
colorList2 = set(["Red", "Green"])

colorList3 = [i for i in colorList1 if i not in colorList2]

print(set(colorList3))
print()


# rozwiązanie w3 resource (ktoś za bardzo je rozbudował, aczkolwiek moje jest poprawne)
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))