f = open('demo10.txt', 'w')
f.write('Welcome to Aptech Django Class. Django is easy to learn and implement.')
f.close()


f1 = open('demo10.txt', 'r')
lines = f1.readlines()

for line in lines:
   s = line.replace('Django', 'Python')
   print(s)
   f2 = open('demo11.txt', 'a')
   f2.write(s)
   f2.close()

f1.close()