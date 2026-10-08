#list17
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

b = sorted(a)

print(b)
print(a)

#list19
n = int(input())

a = []
for i in range(n):
    a.append(input())

print(sorted(a, key=len))
print(max(a, key=len))

#list21
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

positive = [x for x in a if x > 0]

print(positive)
print(len(positive))

#list22
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

d = int(input())

result = [x * d for x in a]
count = len([x for x in a if x == d])

print(result)
print(count)

#list23
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

a = sorted(a, key=abs, reverse=True)

print(a)

#list25
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)

print(a[1])

#list26
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

average = sum(a) / len(a)

result = [x for x in a if x > average]

print(result)
print(f"{average:.1f}")

#list28
n = int(input())

a = []
for i in range(n):
    a.append(input())

letter = input()

result = [s for s in a if s[0] == letter]

print(result)

#list29
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

k = int(input())

result = sorted(a, reverse=True)[:k]

print(result)

#list30
n = int(input())

a = []
for i in range(n):
    a.append(input())

lengths = [len(s) for s in a]

print(lengths)
print(sum(lengths))
