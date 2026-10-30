# ================================================
# ИГРА «СОЛЯНЫЕ ШАХТЫ»
# Автор: Бондаренко София
# Дата: сентябрь 2026
# ================================================

# --- Заголовок ------------------------------------
title = "СОЛЯНЫЕ ШАХТЫ"
frame = "=" * 19
print(frame)
print(" " + title + " ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в соляные шахты. Здесь темно и пахнет сыростью, стены покрыты солью, а впереди слышны странные звуки.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
endurance = int(input())

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // 10 + endurance

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {endurance}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

# --- Главный цикл игры -----------------------------
running = True
actions = 0

while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - прислушаться")
    print("5 - постучать по стене")
    print("6 - тренировка")
    print("0 - выйти из подземелья")

    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()

    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()

    match choice:
        case "0":
            print("Вы поднимаетесь обратно к свету. Соляные шахты остаются позади.")
            running = False
        case "1":
            print("Вы осмотрелись. Стены шахты покрыты белыми разводами соли, "
                  "в углу лежит старая кирка, а на полу — следы чьих-то сапог.")
        case "2":
            cost = 3
            if stamina >= cost:
                stamina -= cost
                print("Вы осторожно идёте вперёд. Соль хрустит под ногами, "
                      "эхо шагов уходит в темноту.")
            else:
                health -= cost - stamina
                stamina = 0
                print("Сил больше нет — вы идёте на одном упорстве. "
                      "Соль режет ноги, но вы не останавливаетесь.")
        case "3":
            stamina = stamina + 2
            print("Вы присели у стены и отдохнули. Дыхание выровнялось, "
                  "силы понемногу возвращаются.")
        case "4":
            print("Вы замерли и прислушались. Где-то в глубине шахты "
                  "капает вода, и слышен тихий скрежет — будто кто-то скребёт камень.")
        case "5":
            stamina = stamina - 1
            print("Вы постучали по стене. Соль осыпалась, и за ней "
                  "обнаружилась небольшая трещина — но разбить стену голыми руками не выйдет.")
        case "6":
            # --- Тренировочный бой ---
            strikes = 6
            total_damage = 0
            crit_count = 0

            print("Вы подходите к глыбе соли, оставшейся от старого обвала.")
            print("На её боку видны вмятины — здесь уже кто-то тренировался.")
            print()
            print(f"Наносите {strikes} ударов.")

            for i in range(1, strikes + 1):
                if i % 3 == 0:
                    hit_damage = crit_damage
                    crit_count += 1
                    print(f"Удар {i}: {hit_damage:.1f} — критический!")
                else:
                    hit_damage = damage
                    print(f"Удар {i}: {hit_damage:.1f}")

                total_damage += hit_damage

            # --- Итог боя ---
            stamina = stamina - 2
            print()
            print(f"Итог: {strikes} ударов, критических ударов: {crit_count}.")
            print(f"Общий урон: {total_damage:.1f}")
            print(f"Средний урон: {total_damage / strikes:.1f}")

    # --- Проверка гибели ---
    if health <= 0:
        print(f"{hero_name} падает без сил. Соляные шахты забирают ещё одного искателя.")
        running = False

    # --- Счётчик действий ---
    if running:
        actions += 1

    # --- Строка состояния ---
    print()
    print(f"Здоровье: {health:4d}   Запас сил: {stamina:4d}")
    print()

# --- Прощание (после цикла) -----------------------
print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)