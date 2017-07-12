def square_of_sum(L):
    sum = 0
    for i in L:
        sum = sum + i * i
    return sum

print (square_of_sum([1, 2, 3, 4, 5]))
print (square_of_sum([-5, 0, 5, 15, 25]))

import math

def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a),( -b - t )/ (2 * a)

print (quadratic_equation(2, 3, 0))
print (quadratic_equation(1, -6, 5))
