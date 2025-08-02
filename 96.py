
#Write a program to count number of lines, words and characters in the file.

try :
 f = open('demo.txt',  'r')
except :
 print('File not found')
else :
#  print(f)
 lines = f.readlines()
#  print(lines)
 print('Number of lines in the file :', len(lines))
 word = 0
 char = 0
 for line in lines :
     words = line.split()
    #  print(words)
     word += len(words)
     for c in words :
         char += len(c)
     
print('Number of words in the file :', word)
print('Number of characters in the file :', char)
 