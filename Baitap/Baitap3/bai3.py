word = list("newfile.txt")
for char in word[::-1]:
    if char == '.':
        word.remove(char)
        break;
    else:
        word.remove(char)
print(word)
#['n', 'e', 'w', 'f', 'i', 'l', 'e']
