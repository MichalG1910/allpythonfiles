a = {}
k = 0
while k < 10:
    # dynamically create key
    key = f'bio{k}'
    # calculate value
    value = k
    a[key] = value 
    k += 1

print(a)

for i in range(0, 3):
    globals()['var_{}'.format(i)] = i * 100
    
print(var_0, var_1, var_2)