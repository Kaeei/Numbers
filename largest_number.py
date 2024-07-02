def largest_number(lst):
    if not lst:
        return None  

# If there is only one element in the list
    if len(lst) == 1:  
        return lst[0]

    # Compare the first number with the largest number in the rest of the list
    return max(lst[0], largest_number(lst[1:]))

# Test example below
print(largest_number([3, 1, 6, 8, 7, 14, 65]))       
