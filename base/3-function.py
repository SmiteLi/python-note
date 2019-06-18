import math

def move( x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = x + step * math.sin(angle)
    return nx, ny

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad oprand type")
    if x >= 0:
        return x
    else:
        return -x

def pass1():
    pass

def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * n
    return s

def add_end(L = None):
    if L is None:
        L = []
    L.append("end.")
    return L


def enroll(name, gender, age=6, city="guangzhou"):
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)

def cal( *number ):
    s = 0
    for n in number:
        s = s + n * n
    return s

def person(name, age, **kw ):
    print("name:",name,"age:",age,"other:",kw)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

print(my_power(9, 3))

print(enroll("lilong", "M"))

print(add_end(['a', 'b', 'c']))

print(cal(10))

print(person('admaa', 45, gender="M", job="IT-MAN"))