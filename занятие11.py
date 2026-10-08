#dict2
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

k = input()

if k in d:
    print(d[k])
else:
    print("нет такого ключа")

#dict3
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

k = input()

print(d.get(k, 0))

#dict5
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

k = input()

d.pop(k, None)

print(len(d))

#dict7
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

best = None

for key in d:
    if best is None or d[key] > d[best]:
        best = key

print(best)

#dict8
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

v = int(input())

print(v in d.values())

#dict9
n = int(input())
d1 = {}

for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value

m = int(input())
d2 = {}

for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value

k = input()

d1.update(d2)

print(len(d1))
print(d1[k])

#dict12
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

reversed_d = {}

for key, value in d.items():
    reversed_d[value] = key

for value, key in reversed_d.items():
    print(f"{value}: {key}")

#dict13
n = int(input())
d = {}

for i in range(n):
    name = input()
    price = int(input())
    quantity = int(input())

    d[name] = [price, quantity]

total = 0
best_name = None
best_cost = -1

for name, data in d.items():
    price, quantity = data
    cost = price * quantity

    total += cost

    if cost > best_cost:
        best_cost = cost
        best_name = name

print(total)
print(best_name)

#dict14
n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

v = int(input())

for key in list(d):
    if d[key] < v:
        del d[key]

print(len(d))

#dict15
n = int(input())
d1 = {}

for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value

m = int(input())
d2 = {}

for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value

ignored = 0

for key, value in d2.items():
    if key in d1:
        ignored += 1
    else:
        d1[key] = value

print(len(d1))
print(ignored)
