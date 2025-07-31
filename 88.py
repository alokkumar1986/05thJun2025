f = open('demo.txt', 'r')
# print(f.read())
# print(f)
for x in f:
    print(x, end='')
    
f.close()