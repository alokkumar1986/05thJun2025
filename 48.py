l = [10, 20, 30, 35, 43, 54]
try:
    print(l[7]) 
except NameError:
    print("Element not found") 
# except IndexError:
#     print("Accessing element at 7th index is out of range")
except :
    print("An unexpected error occurred")
print(l)
print(l[3])