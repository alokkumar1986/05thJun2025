s = "Hello World!"
s1 = s[2:5]
print(s1)  # Output: "llo"

'''
slicing : 
    
    start : index from where to start slicing
    end : index where to stop slicing (not included)
    step : how many characters to skip (default is 1)
'''

s2 = s.split("o")
print(s2)  # Output: ['Hell', ' W', 'rld!']