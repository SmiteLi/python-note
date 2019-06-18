d1 = {"apple":98, "boy":75, "cat": 55 }

for key, value in d1.items():
    print(key," ==> ", value)

s1 = set([1, 2, 3])
print(s1)

s1.add(4)
print(s1)

s2 = set([1, 2, 3, 4, 5])
print("s1 & s2 ",s1 & s2)
print("s1 | s2 ", s1 | s2)
