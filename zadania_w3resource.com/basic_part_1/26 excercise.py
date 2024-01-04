
# Write a Python program to create a histogram from a given list of integers
def histogram(list1):
     list1.sort()
     return list1

print(histogram([1,5,4,9,2,3,45,0,-7,-33,94,124]))

print()
# sortowanie bąbelkowe
list1 = [1,5,4,9,2,3,45,0,-7,-33,94,124]
n = len(list1)
while n > 1:
    zamien = False
    for v in range(0, n-1):
        if list1[v] > list1[v+1]:
            list1[v], list1[v+1] = list1[v+1], list1[v]
            zamien = True
          
    n -= 1
    if zamien == False: break
print(list1)

print()

# rozwiązanie z w3resource
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])




