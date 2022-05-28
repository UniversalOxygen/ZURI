# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    # [assignment] Add your code here
    if(sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")


str1 = input("first word: ", )
str2 = input("second word: ", )


print(">>>>>>>>>")

print("first word: ", str1)
print("second word: ", str2)


print(">>>>>>>>>")

find_anagrams(str1, str2)
# return True
