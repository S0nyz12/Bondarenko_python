#string2
n = int(input())
print(chr(n))

#string3
c = input()
print(chr(ord(c) - 1), chr(ord(c) + 1))

#string4
n = int(input())
s = ""

for i in range(n):
    s += chr(ord("A") + i)

print(s)

#string5
n = int(input())
s = ""

for i in range(n):
    s += chr(ord("z") - i)

print(s)

#string7
s = input()
print(ord(s[0]), ord(s[-1]))

#string8
n = int(input())
c = input()
print(c * n)

#string9
n = int(input())
c1 = input()
c2 = input()

s = ""

for i in range(n):
    if i % 2 == 0:
        s += c1
    else:
        s += c2

print(s)

#string12
s = input()
n = int(input())

print(("*" * n).join(s))

#string14
s = input()
count = 0

for ch in s:
    if "A" <= ch <= "Z":
        count += 1

print(count)

#string15
s = input()
alphabet = "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя"
count = 0

for ch in s:
    if ch in alphabet:
        count += 1

print(count)