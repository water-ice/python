class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k,v in kw.items():#p2 for k,v in kw.iteritems():
            setattr(self,k,v)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print (xiaoming.name)
print (xiaoming.job)


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print (p.name)
#print (p.__score)


class Person(object):
    count = 0
    def __init__(self,name):
        Person.count = Person.count + 1
        self.name = name

p1 = Person('Bob')
print (Person.count)

p2 = Person('Alice')
print (Person.count)

p3 = Person('Tim')
print (Person.count)
