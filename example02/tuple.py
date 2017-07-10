t = ('a',)
print (t);
t2 = ('a', 'b', ['A', 'B'])
x = t2[2]
print(x,t2)
x[0]='x'
x[1]='y'#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
print(t2)
