#1. values() 方法实际上把一个 dict 转换成了包含 value 的list。
#2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。
#3. 打印 itervalues() 发现它返回一个 <dictionary-valueiterator> 对象，这说明在Python中，for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
# print d.itervalues()
# <dictionary-valueiterator object at 0x106adbb50>
for v in d.values():
    print (v)

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for i in d.values():
    sum = sum + i
print (sum/len(d))

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print (k , ':', v)
print ('average', ':', sum /len(d))
