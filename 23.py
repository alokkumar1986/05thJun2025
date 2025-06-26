'''
price = 100
#s = "The price is : "+price
s = f"The price is : {price}"

print("The price is : ", price)
print(s)
'''

item = "Rice"
price = 50
unit = 'Kg'

#s = "I bought 1kg of rice with 50 Rupees"
s = f"I bought 1{unit} of {item} with {price} Rupees"

print(s)