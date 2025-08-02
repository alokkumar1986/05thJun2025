# program to get duplicate elements in a list
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:        
        if item in seen:
            duplicates.add(item)
        else:   
            seen.add(item)
    return list(duplicates)     

# Example usage
my_list = [1, 2, 3, 4, 5, 1, 2, 6]  

duplicates = find_duplicates(my_list)
print("Duplicate elements:", duplicates)