import platform
import random


'''
def f (str):
    for i in range (1,3):
        yield i

a = f(4)
print(a.__iter__())
print(a.__next__())
print(a.__next__())
class A:
    def a(self):
        print("A", end="")
    def b(self):
        self.i()


    def i(self):
        print("11qawe")



class B(A):
    def a(self):
        print("B", end="")
    def do(self):
        self.b()

    def i(self):
        print("qawe")

def even(x):
    return x %2 == 0

a = [a for a in range(5)]
b = list (filter(lambda x: x % 2, a))
print(a,b)





class Class:
    __var= 0
    def foo(self):
        Class._Class__var +=1
        self.__prop=Class._Class__var

o1 = Class()
o1.foo()

print(o1._Class__prop, o1._Class__var)
o2= Class()
o2.foo()

print(o2._Class__prop, o2._Class__var, o1._Class__prop)

class myclass:
    def __init__(self):
        self.que = [1,2]

    def get(self):
        return self.que


    def last(self):
        return self.que[-1]

    def add(self):
        self.que.append(self.que[-1]+1)



a = myclass()
a.add()
a.add()
print(a.get())#


class CA:
    var = 1
    def __init__(self,p):
        p1 =p2=p

class CB(CA):
    def __init__(self,prop):
        prop3 = prop ** 2
        super().__init__(prop)
    def __str__(self):
        return "Object"

def add(a,b,/,*,c,d):
    print(a+b+c+d)

add(2,3,c=3,d=5)

def f(n):
    for i in range(1,n+1):
        yield i

a = f(3)
print(a.__next__())
print(a.__next__())
print(next(a,33))

for n in f(1):
    print(n)

list = [i for i in range(1,5)]
print(list)

# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

print(mutable_bytes)
# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)

a= "wewe0".encode("utf-8")
print(a)


a= 16
b= a.to_bytes(1,"big",signed=False)
c=a.to_bytes(2,"big",signed=True)
print(b,c)
int()

class Player:
    # class variables
    club = 'Chelsea'
    sport = 'Football'

    def __init__(self, name):
        # Instance variable
        self.name = name

    def show(self):
        print("Player :", 'Name:', self.name, 'Club:', self.club, 'Sports:', self.sport)

p1 = Player('John')

# wrong use of class variable
Player.club= "qw"
p1.show()

p2 = Player('Emma')
p2.sport = 'Tennis'
p2.show()

def my_deco(coating):
    """ tihi funkion """
    def wrapper1(func1):
        def wrapper2(*args):
            func2(*args)
        return wrapper2
    return wrapper1


print(my_deco.__doc__)
a = [1,2,3]
b= [5,6,7,8,9,10]
c= zip(b,a)
print(dict(c))
y = (lambda x: x*10 +5) (3)
print(y)


'''
'''

function Animal(){
    this.sound = "ee"
}
Animal.prototype.makeSound = function(){
    console.log(this.sound);
}
function Dog(){
    this.sound ="wau wau"
}

Dog._____ = new Animal()

var dog = new Dog()
dog.makeSound()




a = 5
b= {'a':1,"b":2}
print(type(a))
print(type(b))
print(a.__class__)



def f (obj):
    print(obj.attr)

Foo = type('Foo',(),{'attr':100,'val':f})

x = Foo()
print(x.attr)
x.val()

import random
import sys


class apple():
    totalapple = 0
    totalweight = 0

    def __init__(self, weight):

        if apple.totalapple == 1000 or apple.totalweight == 300:
            print("done mit {} apples und {} gewicht".format(apple.totalapple, apple.totalweight))
        apple.totalapple += 1
        apple.totalweight += weight




for i in range(1008):
    apple(random.uniform(0.2, 0.3))

print (apple.totalapple)



class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight
    def _test(self):
        pass

p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)

dic = {1:133,2:2,3:3,4:4}
print(133 in dic.values())

import math

class TimeTellsNoLies():
    def __init__(self,hour=int,minute=int,sec=int):
        self.hour = hour
        self.minute = minute
        self.sec = sec
        self.totalsec = self.hour * 60 * 60 + self.minute * 60 + self.sec

    def __add__(self, other):
        if type(other) == int:
            return "addd"
        else:
            endSecs = self.totalsec + other.totalsec
            endhour = endSecs / 3600
            print(endhour)
            endminute = endhour %1
            endminute *= 60
            print(endminute)
            endsec = endminute %1
            endsec = endsec * 60
            print(endsec)
            return ("{}HH:{}MM:{}SS".format(math.floor(endhour),round(endminute),round(endsec)))



    def __sub__(self, other):
        endSecs = self.totalsec - other.totalsec
        endhour = endSecs / 3600
        print(endhour)
        endminute = endhour %1
        endminute *= 60
        print(endminute)
        endsec = endminute %1
        endsec = endsec * 60
        print(endsec)
        return ("{}HH:{}MM:{}SS".format(math.floor(endhour),round(endminute),round(endsec)))


    def __mul__(self, other):
        endSecs = self.totalsec * other
        endhour = endSecs / 3600
        print(endhour)
        endminute = endhour %1
        endminute *= 60
        print(endminute)
        endsec = endminute %1
        endsec = endsec * 60
        print(endsec)
        return ("{}HH:{}MM:{}SS".format(math.floor(endhour),math.floor(endminute),math.floor(endsec)))

    def __str__(self):
        return "lalala"

    def secInts(self, secs):
        endSecs = self.totalsec + secs
        endhour = endSecs / 3600
        print(endhour)
        endminute = endhour % 1
        endminute *= 60
        print(endminute)
        endsec = endminute % 1
        endsec = endsec * 60
        print(endsec)
        return ("{}HH:{}MM:{}SS".format(math.floor(endhour), math.floor(endminute), math.floor(endsec)))
  #   print("done mit {} apples und {} gewicht".format(apple.totalapple, apple.totalweight))


a = TimeTellsNoLies(21,58,50)
b = TimeTellsNoLies(1,45,22)

print(a +b)

def test(first,sec):
    print(first,sec)

test(sec=5,first=99)


def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print(1)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    return wrapper


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print(12)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)



pack_books('Alice in Wonderland', 'Winnie the Pooh')
#pack_toys('doll', 'car')
#pack_fruits('plum', 'pear')



from datetime import datetime

timestamp = datetime.now()


string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

class timedeco():
    def __init__(self,mat):
        self.mat = mat

    def __call__(self,func):
        def intwrap(*arg,**kwargs):
            print(self.mat)
           # self.func = func
            print(string_timestamp)
            print(func(*arg))
        return intwrap



def timedecorator(*kargs):
        def wrapper(original_function):
            def internalwarp(*args):
                #print(original_function(*args))
                print(string_timestamp)
            return internalwarp
        return wrapper

a = timedeco(21431)

@timedeco('qewqew')
def add(a,b,*qwe):
    return (a+b),


add(5,3,66)

'''

