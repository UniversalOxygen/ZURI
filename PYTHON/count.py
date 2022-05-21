count = 0
sentence = input("Enter your sentence: ")

for space in sentence:
    if space == " ":
        count += 1
number_of_words = count + 1
print("Number of words : ", number_of_words)
