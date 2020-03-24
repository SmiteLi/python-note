

classmates = ["tom", "cat", "apple"]

classmates.append('boye')
classmates.insert(2, 'doge')

print("use pop() to delete the last element.")

classmates.pop()


L = ['apple', 123, True]

for index in range(len(classmates)):
    print("the classmate : " + classmates[index])

t1 = (1, )
t2 = ('a', 'b', ['aaa', 'bbb'])

for e in t2:
    print('the element of t2 : ' + str(e))