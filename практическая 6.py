#err2
a = int(input())
b = int(input())
try:
    result = a / b
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(f"{result:.1f}")

#err5
word = input()
index = int(input())
try:
    print(word[index])
except IndexError:
    print("Нет такого символа")

#err6
word = input()
try:
    index = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    try:
        print(word[index])
    except IndexError:
        print("Нет такого символа")

#err7
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")
print(number)

#err9
try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
except ValueError as e:
    print("Отклонено:", e)
else:
    print("Принято:", age)

#err11
try:
    a = int(input())
    b = int(input())
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")

#err12
try:
    number = int(input())
except ValueError as e:
    print(e)
    print(type(e))
else:
    print(number)
