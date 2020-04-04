# 缩排使用4个空格，没有制表符
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

for e in classmates:
    print("tom is " + e)
    # is 对对象的内存地址比较，相同则是同样的对象
    print("tom" is e)

print(t1 is not None, t2 is None)

# in and 'not in'
print(1 in t1)
print(1 not in t2)

num = 5     
if num == 3:            # 判断num的值
    print('boss')        
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')     # 条件均不成立时输出

while num < 10:
    print(num)
    num +=1

i = input("input a integer: ")
try:
    i = int(i)
    print("valid integer entered:",i)
except ValueError as err:
    print(err)

