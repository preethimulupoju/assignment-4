numbers = (1,2,3,4,5,6,7)
print("OG: ", numbers)
result = map(lambda x: x + x + x, numbers)
print("\nTriple of said list numbers:")
print(list(result))
