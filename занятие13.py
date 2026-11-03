#matrix2
m = int(input())
n = int(input())

a = []

for i in range(m):
    row = []
    for j in range(1, n + 1):
        row.append(5 * j)
    a.append(row)

for row in a:
    print(row)

#matrix3
m = int(input())
n = int(input())
values = [int(x) for x in input().split()]

a = []

for i in range(m):
    row = [values[i]] * n
    a.append(row)

for row in a:
    print(row)

#matrix5
m = int(input())
n = int(input())
d = int(input())
values = [int(x) for x in input().split()]

a = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(values[i] + d * j)
    a.append(row)

for row in a:
    print(row)

#matrix6
m = int(input())
n = int(input())
q = int(input())
values = [int(x) for x in input().split()]

a = []

for i in range(m):
    row = [x * (q ** i) for x in values]
    a.append(row)

for row in a:
    print(row)

#matrix10
m = int(input())
n = int(input())

a = []

for i in range(m):
    row = [int(x) for x in input().split()]
    a.append(row)

for j in range(0, n, 2):
    for i in range(m):
        print(a[i][j])
        