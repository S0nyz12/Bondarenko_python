#while2
a = int(input())
b = int(input())

free = a
count = 0

while free >= b:
    free -= b
    count += 1

print(count)

#while4
n = int(input())
rest = n

while rest % 3 == 0:
    rest //= 3

print(rest == 1)

#while5
n = int(input())

k = 0
while n > 1:
    n //= 2
    k += 1

print(k)

#while6
n = int(input())

result = 1.0
while n >= 1:
    result *= n
    n -= 2

print(result)

#while7
n = int(input())

k = 0
while (k + 1) * (k + 1) <= n:
    k += 1

print(k + 1)

#while9
n = int(input())

power = 1
k = 0

while power <= n:
    power *= 3
    k += 1

print(k)

#while10
n = int(input())

power = 1
k = 0

while power * 3 < n:
    power *= 3
    k += 1

print(k)

#while12
n = int(input())

total = 0
k = 0

while total + (k + 1) <= n:
    k += 1
    total += k

print(k)
print(total)

#while13
a = float(input())

total = 0.0
k = 0

while total <= a:
    k += 1
    total += 1 / k

print(k)
print(total)

#while14
a = float(input())

total = 0.0
k = 0

while total + 1 / (k + 1) < a:
    k += 1
    total += 1 / k

print(k)
print(total)