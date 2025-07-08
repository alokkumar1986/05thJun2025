num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try: 
  div = num1 / num2
except ZeroDivisionError:
  print("Second number can not be zero")
else: 
  print(f"The division of {num1} by {num2} is {div}")