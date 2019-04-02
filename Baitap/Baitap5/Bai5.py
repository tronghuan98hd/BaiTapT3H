L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]
S1 = set(L1)
S2 = set(L2)
print(S1.intersection(S2))
print(S1.difference(S2))
print(S2.difference(S1))
print(S1.symmetric_difference(S2))

'''
{3, 4, 5, 6}
{1, 2}
{8, 9, 10, 7}
{1, 2, 7, 8, 9, 10}
'''
