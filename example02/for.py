L = [75, 92, 59, 68]
sum = 0.0
for i in L:
    sum = sum + i
print (sum / 4)

sum = 0 #while
x = 1
while x < 100:
    sum = sum + x
    x= x + 2
print (sum)

sum = 0  #break
x = 1
n = 1
while True:
    sum = sum + x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print (sum)

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 ==0:
        continue
    sum = sum + x
print (sum)

#对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [ 0,1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if x < y:
            print(x*10 + y)
