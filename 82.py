# def findQube(num):
#   return num*num*num

findQube = lambda num : num*num*num

num = int(input('Enter a number : '))

print('Qube of {} is '.format(num), findQube(num))


