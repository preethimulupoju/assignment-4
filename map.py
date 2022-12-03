def square_num(n):
    return n * n
numbers = [4,5,2,9]
print("original list: ",numbers)
result = map(square_num, numbers)
print("square the elements of the said list using map():")
print(list(result))
