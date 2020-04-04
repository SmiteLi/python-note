import sys, random

def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)

print('enter a numuber')

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError as err:
        break


if count:
    print("count=", count, "total=", total, "mean = ", total / count)

# age = get_int("enter your ages:")

print(sys.argv)