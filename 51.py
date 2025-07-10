#Write a program to generate six digit OTP.
import random as ran  # Module
               # randint() function is used to generate random numbers
            
# import module1 as m

# print(m.greeting("Aptech"))

# print(m.greeting(m.person['name']))

print("OTP : " ,ran.randint(0, 9),ran.randint(0, 9), ran.randint(0, 9),ran.randint(0, 9),ran.randint(0, 9),ran.randint(0, 9)) 