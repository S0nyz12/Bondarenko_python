#Boolean2
a = int(input())

print(a % 2 != 0)

#Boolean3
a = int(input())

print(a % 2 == 0)

#Boolean4
a = int(input())
b = int(input())

print(a > 2 and b <= 3)

#Boolean5
a = int(input())
b = int(input())

print(a >= 0 or b < -2)

#Boolean7
a = int(input())
b = int(input())
c = int(input())

print((a < b < c) or (c < b < a))

#Boolean8
a = int(input())
b = int(input())

print(a % 2 != 0 and b % 2 != 0)

#Boolean9
a = int(input())
b = int(input())

print(a % 2 != 0 or b % 2 != 0)

#Boolean10
a = int(input())
b = int(input())

count = (a % 2 != 0) + (b % 2 != 0)

print(count == 1)

#Boolean11
a = int(input())
b = int(input())

print(a % 2 == b % 2)

#Boolean13
a = int(input())
b = int(input())
c = int(input())

print(a > 0 or b > 0 or c > 0)

#Boolean15
a = int(input())
b = int(input())
c = int(input())

count = (a > 0) + (b > 0) + (c > 0)

print(count == 2)

#If1
number = int(input())

if number > 0:
    number += 1

print(number)

#If2
number = int(input())

if number > 0:
    number += 1
else:
    number -= 2

print(number)

#If3
number = int(input())

if number > 0:
    number += 1
elif number < 0:
    number -= 2
else:
    number = 10

print(number)

#If4
a = int(input())
b = int(input())
c = int(input())

count = (a > 0) + (b > 0) + (c > 0)

print(count)

#If5
a = int(input())
b = int(input())
c = int(input())

positive_count = (a > 0) + (b > 0) + (c > 0)
negative_count = (a < 0) + (b < 0) + (c < 0)

print(positive_count)
print(negative_count)