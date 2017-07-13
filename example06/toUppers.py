def toUppers(L):
    return[x.upper() for x in L if isinstance(x,str) ]

print (toUppers(['Heldlo', 'world', 101]))
