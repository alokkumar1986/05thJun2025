# a, b = input("Enter two numbers separated by space: ").split()
# print("Sum is:", int(a)+int(b))

'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)
'''

#Write a program to enter your name through keyboard and find the number of characters in it.

name = input("Enter your name: ")
print("The number of characters in ", name, " is :", len(name))
print("The number of characters in {} is : {}".format(name, len(name)))

#{} : replace with the value of the variable inside the string

print("a = {}, b = {}, c = {}".format(10, 1.25, "Aptech"))