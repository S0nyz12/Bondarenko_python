#proc17
def roots_count(a, b, c):
    d = b * b - 4 * a * c

    if abs(d) < 1e-9:
        return 1
    if d > 0:
        return 2
    return 0

for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())

    print(roots_count(a, b, c))

#proc18
def circle_s(r):
    return 3.14 * r * r

for i in range(3):
    r = float(input())
    print(circle_s(r))

#proc20
import math

def triangle_p(a, h):
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    return a + 2 * b

for i in range(3):
    a = float(input())
    h = float(input())

    print(triangle_p(a, h))

#proc21
def sum_range(a, b):
    if a > b:
        return 0

    return sum(range(a, b + 1))

a = int(input())
b = int(input())
c = int(input())

print(sum_range(a, b))
print(sum_range(b, c))

#proc23
def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

for i in range(3):
    x = float(input())
    y = float(input())

    print(quarter(x, y))

#proc24
def even(k):
    return k % 2 == 0

count = 0

for i in range(10):
    k = int(input())

    if even(k):
        count += 1

print(count)

#proc25
import math

def is_square(k):
    if k <= 0:
        return False

    r = int(math.sqrt(k))

    return r * r == k or (r + 1) * (r + 1) == k

count = 0

for i in range(10):
    k = int(input())

    if is_square(k):
        count += 1

print(count)

#proc26
def is_power5(k):
    if k <= 0:
        return False

    while k % 5 == 0:
        k //= 5

    return k == 1

count = 0

for i in range(10):
    k = int(input())

    if is_power5(k):
        count += 1

print(count)

#proc27
def is_power_n(k, n):
    if k <= 0 or n <= 1:
        return False

    while k % n == 0:
        k //= n

    return k == 1

n = int(input())
count = 0

for i in range(10):
    k = int(input())

    if is_power_n(k, n):
        count += 1

print(count)

#proc29
def digit_count(k):
    count = 0

    while k > 0:
        count += 1
        k //= 10

    return count

for i in range(5):
    k = int(input())
    print(digit_count(k))