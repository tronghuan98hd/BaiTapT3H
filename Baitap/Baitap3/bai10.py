import string
alphabets = string.ascii_lowercase
words = {"python", "patience", "document", "student", "homework",
       "practice", "success", "english", "university", "congratulation"}
result = []
for word in words:
    sum = 0
    for i in list(word):
        sum += alphabets.index(i) + 1
    result.append([word,sum])
print(result)

#[['document', 95], ['homework', 108], ['university', 162], ['english', 74], ['success', 89], ['patience', 73], ['python', 98], ['congratulation', 170], ['practice', 75], ['student', 103]]

