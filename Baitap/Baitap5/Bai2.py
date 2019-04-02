file = open("test.txt")
f = tuple(file)
file.close()
print(f[-1:-10:-1])

'''
('29999999\n', '29999998\n', 'Fizz\n', '29999996\n', 'Buzz\n', 'Fizz\n', '29999993\n', '29999992\n', 'Fizz\n')
'''
