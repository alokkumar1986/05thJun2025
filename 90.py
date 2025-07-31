
try:
 f = open('demo3.txt', 'x')
except FileExistsError:
 print("File already exists.")