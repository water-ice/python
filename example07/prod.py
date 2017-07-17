from functools import reduce#2与3的不同
def prod(x, y):
    return x * y

print (reduce(prod, [2, 4, 5, 7, 12]))
