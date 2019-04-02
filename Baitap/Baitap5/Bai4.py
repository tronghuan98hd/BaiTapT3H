words = []
lines = Data.rsplit('\n')
for line in lines:
    for word in line.split(" "):
        words.append(word)
S = set(words)
result = [(word, len(word)) for word in S if len(word) > 10]
print(result)

#[('https://www.python.org/,', 24), ('programming', 11), ('interpreted', 11), ('object-oriented', 15), ('distributions', 13), ('implemented', 11), ('application', 11), ('description', 11), ('development', 11), ('Interpreter', 11), ('interpreter', 11), ('programming.', 12), ('experience,', 11), ('distributed.', 12), ('customizable', 12), ('comprehensive', 13), ('self-contained,', 15), ('applications.', 13), ('documentation.', 14)]

