# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入
# 的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
# 需要用list()函数获得所有结果并返回list。
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'C', None, ' '])))

# 构造一个从3开始的奇数序列：

def _odd_iter():
    n =1
    while True:
        yield n+2

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

print(sorted([36, 5, -12, 9, -21]))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))