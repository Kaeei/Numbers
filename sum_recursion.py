def sum_up_to(lst, index):
    if index == 1:
        return lst[0]
    return lst[index] + sum_up_to(lst, index - 1)

# Test the function with examples
print(sum_up_to([1, 4, 34, 46, 12, 16], 4))  
print(sum_up_to([4, 7, 13, 8], 1))  