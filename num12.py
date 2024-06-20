def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)


print(sum_of_even(5))   
print(sum_of_even(10)) 
print(sum_of_even(100))
