d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print (d);

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print ('Adam:',d['Adam'])
print ('Lisa:',d['Lisa'])
print ('Bart:',d['Bart'])
#dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。
#dict的第二个特点就是存储的key-value序对是没有顺序的！
#dict的第三个特点是作为 key 的元素必须不可变，

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print (key + ':' , d[key])
