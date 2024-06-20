def same_data_type(lst):
    if len(lst) == 0:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

print(same_data_type([1, 2, 3]))      
print(same_data_type([1, 2, '3']))    
