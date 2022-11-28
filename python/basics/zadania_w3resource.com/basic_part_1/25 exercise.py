
# Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
values = [1,5,8,3]
def isSheValues(n):
    if n in values:
        return True
    else:
        return False

print(isSheValues(3))
print(isSheValues(-1))

print()

# rozwiązanie w3resource
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

