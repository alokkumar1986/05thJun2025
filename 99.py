f = open('demo.txt', 'r')
f1 = open('demo_copy.txt', 'w')

for x in f:
 f1.write(x)

f.close()
f1.close()