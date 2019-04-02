f = open("test.txt", "w")
for i in range(1, 30000000):
    if i % 15 == 0:
        f.write("FizzBuzz\n")
    elif i % 3 == 0:
        f.write("Fizz\n")
    elif i % 5 == 0:
        f.write("Buzz\n")
    else:
        f.write("{}\n".format(i))
f.close()
