def all_unique(lst):
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 3, 4, 5]))      
print(all_unique([1, 2, 3, 3, 4, 5]))   
