# https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080

def f(x):
    return x * x

print(list(range(10)))
r = map(f, list(range(10))) # r is a Iterator
print(r)

print(list(r))

print(list(map(str, list(range(1, 25)))))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
   digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
   return digits[s]

print(reduce(fn, map(char2num, '13579')))

