# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# def read_file_content(filename):

# [assignment] Add your code here
l = input("enter the string: ")
d = {}
print(l)
for i in l:
    if i not in d:
        d[i] = l.count(i)
    else:
        pass
print("Frequency of each element-")

for k in d:
    print(k, "-", d[k])
