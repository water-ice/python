def f1(x):
    return x

def new_fx(f):
    def fn(x):
        print ('call ' + f.__name__ +'()')
        return f1(x)
    return fn

g = new_fx(f1)
print(g(5))


import time
from functools import reduce
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print ('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print (factorial(10))
