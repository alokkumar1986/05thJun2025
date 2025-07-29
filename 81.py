# def findSquare(num):
#   return num*num

findSquare = lambda num : num*num

num = int(input('Enter a number : '))

print('Square of {} is '.format(num), findSquare(num))