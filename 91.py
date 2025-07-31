try : 
 f = open('demo.txt', 'r')
except :
 print('File not found')
else :
  print(f.readline())
  print(f.readline())
  print(f.readline())
