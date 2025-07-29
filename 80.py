
# def findOddEven(num):
#   return 'Even' if num%2==0 else 'Odd' 

findOddEven = lambda num :  'Even' if num%2==0 else 'Odd'

num = int(input('Enter a number : '))

print(num, ' is ', findOddEven(num))