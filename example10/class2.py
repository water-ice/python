class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = L1.sort(key=lambda p1,p2:cmp(p1.name,p2.name), reverse=True)

print (L2[0].name)
print (L2[1].name)
print (L2[2].name)
