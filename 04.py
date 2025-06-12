# Write a program to print all the keywords in Python
import keyword 

# Print all the keywords in Python
keywords = keyword.kwlist 
for i in keywords:
    print(i, end=' ')