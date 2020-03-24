import os

print([d for d in os.listdir('.')])

L = ["one", "two", "three", "four", "five"]

print(L[0:3])

print(L[:3])

print(L[-2:])

L1 = list(range(100))

print(L1[:10])

print(L1[:10:2])

print(L1[::5])

str1 = 'abcdefghijklmn'

print(str1[::2])

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, " ==> ", v)

for i, value in enumerate(d):
    print(i, value)

for x, y in [(1,1), (2,2), (3,3)]:
    print(x, y)

L2 = [x * x for x in range(1,11)]
print(L2)

L3 = [x * x for x in range(1, 22) if x%2 == 0]
print(L3)

L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L4)

L5 = ["Hello", "World!", "IBM", "Apple"]
print([s.lower() for s in L5])