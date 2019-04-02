L = [[1,2,3],[4, [5, 6, [7]], 8], 9, 10]
output = []
def flatten_list(L):
    for i in L:
        if type(i) == list:
            flatten_list(i)
        else:
            output.append(i)
    return output
print(flatten_list(L))

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

