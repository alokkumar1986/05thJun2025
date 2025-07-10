# from add import add as a, subtract as s

import add as a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# print("Addition:", a(num1, num2))
# print("Subtraction:", s(num1, num2))

print("Addition:", a.add(num1, num2))
print("Subtraction:", a.subtract(num1, num2))