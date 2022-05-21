print("WELCOME TO OXYGEN SIMPLE CALCULATOR")
print("Please input your values...")

A = int(input("input first value:- "))
B = int(input("input second value:- "))

sum = (A + B)
sub = (A - B)
mul = (A * B)
div = (A / B)

Operation = input(
    "what operation will you like to perform?\nPick any of ['+', '-', '*', '/']: ")
print(">>>")
print(">>>>>>")
print(">>>>>>>>>")
if Operation == '+':
    print("The sum of the values:- ", sum)
elif Operation == '-':
    print("The Difference of the values:- ", sub)
elif Operation == '*':
    print("The Product of the values:- ", mul)
elif Operation == '/':
    print("The Division of the values:- ", div)
else:
    print("Invalid operation, try again...")
