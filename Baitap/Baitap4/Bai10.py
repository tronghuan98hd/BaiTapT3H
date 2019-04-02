from string import ascii_lowercase
words = ['python', 'patience', 'documents', 'students',
      'homework', 'practice', 'success', 'english',
      'university', 'congratulation' ]

list_words = []
for word in words:
    values = 0
    for char in word:
        value = ascii_lowercase.index(char) + 1
        values = values + value
    list_words.append([word, values])

print(list_words)

#[['python', 98], ['patience', 73], ['documents', 114], ['students', 122], ['homework', 108], ['practice', 75], ['success', 89], ['english', 74], ['university', 162], ['congratulation', 170]]

