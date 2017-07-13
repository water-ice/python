L = list(range(1,101))

print (L)
print (L[:10])
print (L[2::3])
print (L[4:50:5])
print (L[-10:])#最后10个
print (L[-46::5])#最后10个5的倍数

def firstCharUpper(s):
    f = s[:1].upper()
    l = s[1:]
    return f + l

print (firstCharUpper('hello'))
print (firstCharUpper('sunday'))
print (firstCharUpper('september'))
