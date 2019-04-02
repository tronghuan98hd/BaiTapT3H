L = [7,5,7,2,4,1,0,7,3,5,6,12,25,2,42,0,9]
max = min = L[0]
for i in L:
    if i < max:
        min = i
    else:
        max = i
print(max, min)

#42 9

