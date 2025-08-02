#1)
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
sum = num1+num2
print('Sum is ', sum)

#2)
def findSum(num1, num2):
  print('Sum is ', num1+num2)

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
findSum(num1, num2)

#3) 

class NumberSum :
  num1 = 0
  num2 = 0
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def findSum(self):
    print('Sum is ', self.num1+self.num2)

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
p = NumberSum(num1, num2)
p.findSum()
