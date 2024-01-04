
# Write a Python program to count the number 4 in a given list.

list1 = (1,2,3,4,5,6,7,8,4,4)
print(list1.count(4))

print()

# rozwiązanie z w3resource

def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))