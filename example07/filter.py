import math

def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r ==x

print (list(filter(is_sqr, range(1, 100))))
