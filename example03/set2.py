s = set(['Adam', 'Lisa', 'Paul','x'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for i in L:
    if i in s:
        s.remove(i)
    else:
        s.add(i)
print (s)
