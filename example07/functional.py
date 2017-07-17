#把计算视为函数而非指令
#纯函数式编程：不需要变量，没有副作用，测试简单
#支持高阶函数，代码简洁
f = abs
print(f(-2))

def add(x,y,f):
    return f(x) + f(y)

print(add(3,-5,abs))


import math

def add(x, y, f):
    return f(x) + f(y)

print (add(25, 9, math.sqrt))
