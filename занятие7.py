#list2
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

k = int(input())

print(a[k])
print(a[-1])
print(k)

#list3
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

s = 0
p = 1

for i in range(n):
    s += a[i]
    if i % 2 == 0:
        p *= a[i]

print(s)
print(p)

#list5
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

d = int(input())

a.append(d)

print(a)
print(len(a))

#list7
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

print(a[::-1])
print(a)

#list9
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

s = 0
for x in a:
    s += x

average = s / len(a)

count = 0

for x in a:
    if x > average:
        print(x, end=" ")
        count += 1

print()
print(count)

#list10
n = int(input())

a = []
for i in range(n):
    a.append(input())

imax = 0
imin = 0

for i in range(1, len(a)):
    if len(a[i]) > len(a[imax]):
        imax = i

    if len(a[i]) < len(a[imin]):
        imin = i

print(a[imax])
print(a[imin])
print(len(a[imax]))
print(len(a[imin]))

#list12
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

k = int(input())

a.insert(k, 0)

print(a)
print(len(a))

#list13
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

x = a.pop()

print(x)
print(a)

#list14
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

d = int(input())

print(a.count(d))

if d in a:
    print(a.index(d))
else:
    print(-1)

#list15
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

s = 0

for i in range(1, len(a), 2):
    print(a[i], end=" ")
    s += a[i]

print()
print(s)
