
#form2 : print() with a string argument
s = 'Aptech Learning'
print(s)  #Aptech Learning

# form3 : print() with a variable argument
a = 10
print(a)  #10

# form4 : print() with multiple arguments

a = 10
b = 20
c = 30
print(a, b, c)  #10 20 30

# form5 : print() with a string and a variable argument
a = 10
print("The value of a is : ", a)  #The value of a is : 10


#a= 10, b= 20, c= 30
print("a= ", a, ", b= ", b, ", c= ", c)  #a= 10, b= 20, c= 30   

# form6 : print() with a string and multiple variable arguments
print("The values are : ", a, b, c)  #The values are : 10 20 30

# form7 : print() with a string and multiple variable arguments with sep and end
print("The values are : ", end ="")
print(a, b, c, sep=', ')  #The values are : 10 , 20 , 30.

#The values are : 10 - 20 - 30

print("The values are : ", end="")
print(a, b, c, sep=' - ')  #The values are : 10 - 20 - 30

#form8 : print() with a string and multiple variable arguments with end

# 1 11 111 1111
n = 5
for i in range(1, n + 1):
    print('1' * i, sep="-",  end=" ")  #Prints 1, 11, 111, 1111, 11111  
    
#form9 : print() with a string and multiple variable arguments with end and sep 
print("The values are : ", end="")
print(a, b, c, sep=' - ')  #The values are : 10 - 20 - 30


print("The values are : \n",a, b,c)


lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(lorem_ipsum)  #Prints the lorem ipsum text