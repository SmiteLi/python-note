# dict内部存放的顺序和key放入的顺序是没有关系的。
d1 = {"apple":98, "boy":75, "cat": 55 }
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'long':100}
print(d['Michael'])
d['boy'] = 99

if 'Bob' in d:
    print("'Thomas' in d : " , 'Thomas' in d)

print(d.get('Thomas', "not exist!"))
print(d)
d.pop('long')
print(d)

for key, value in d1.items():
    print(key," ==> ", value)




s1 = set([1, 2, 3,4,5,6,7,7,7,8,8,9])
print(s1)

s1.add(10)
print(s1)

s1.remove(8)
print(s1)

s2 = set([1, 2, 3, 4, 5])
print("s1 & s2 ",s1 & s2)
print("s1 | s2 ", s1 | s2)

