from collections import Iterable

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

from collections import Iterator

print(isinstance([], Iterator))

print(isinstance([x for x in range(10)], Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

print(isinstance(iter([]) , Iterator))

print(isinstance(iter('abc') , Iterator))

L = [x *x for x in range(10)]

g = (x * x for x in range(10))

print(L)
print(g)
print(next(g))

for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return "done"

print(fib(6))
for n in fib(6):
    print(n)