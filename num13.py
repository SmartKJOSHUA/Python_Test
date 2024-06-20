def evens_and_odds(n):
    evens = sum(1 for i in range(1, n+1) if i % 2 == 0)
    odds = n - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))

