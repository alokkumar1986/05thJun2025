import os 

if os.path.exists('demo2.txt'):
  os.rename('demo2.txt', 'demo3.txt')
else:
  print('File not found')
  

#===========================================
  
os.remove('demo3.txt')

f = open('demo2.txt', 'x')

os.mkdir('new_directory')
os.rmdir('new_directory')