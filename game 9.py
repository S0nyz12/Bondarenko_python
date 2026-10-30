# ================================================
# ИГРА «СОЛЯНЫЕ ШАХТЫ»
# Автор: Бондаренко София
# Дата: сентябрь 2026
# ================================================

import random

# --- Заголовок ------------------------------------
title = "СОЛЯНЫЕ ШАХТЫ"
frame = "=" * 19

# --- Правила игры ---------------------------------
base_attack = 10
damage = 0          
crit_damage = 0     

# --- Враги и журнал боя ----------------------------
enemies = ["скелет", "гуль", "паук", "летучая мышь", "соляной голем"]
log = []  


# ==================================================
# ФУНКЦИИ ПРАВИЛ
# ==================================================

def hero_hit(strike_n):
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health):
    enemy_hp = 45.0
    rounds = []
    round_n = 0

    print(f"Вы спускаетесь по лестнице. Из темноты появляется {enemy}!")

    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        enemy_hp -= hit

        line = f"Раунд {round_n}: вы наносите {hit:.1f} урона"
        if crit:
            line += " — критический!"

        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += (f" Здоровье {enemy}: {enemy_hp:.1f}. "
                     f"{enemy.capitalize()} бьёт в ответ на {blow}.")
            rounds.append([round_n, hit, blow])

        print(line)

    return rounds, enemy_hp <= 0, hero_health


def print_leaderboard(log):
    if not log:
        print("Вы ещё не сражались. Таблица лидеров пуста.")
        return

    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")

    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге не было боёв.")


# ==================================================
# СЮЖЕТ
# ==================================================

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

while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        endurance = int(input())

        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or endurance < 0:
            raise ValueError("Сила, ловкость и выносливость не могут быть отрицательными")
        if strength > 20:
            raise ValueError(f"Сила не может превышать 20, а введено {strength}")

        break
    except ValueError as e:
        print(f"{e}. Введите все четыре числа снова:")

# --- Расчёт урона ----------------------------------
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
menu_last = 8
outcome = "прерывание"

try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - прислушаться")
        print("5 - постучать по стене")
        print("6 - тренировка")
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("0 - выйти из подземелья")

        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")

        match choice:
            case "0":
                print("Вы поднимаетесь обратно к свету. Соляные шахты остаются позади.")
                outcome = "выход"
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
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage

                # --- Итог боя ---
                stamina = stamina - 2
                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
            case "7":
                # --- Спуск глубже и бой с врагом ---
                if not enemies:
                    print("Вы спускаетесь по лестнице, но подземелье пусто. "
                          "Здесь больше не с кем сражаться.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health = fight(enemy, health)

                    for r in rounds:
                        log.append(r)

                    if won:
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} побеждён! В подземелье осталось врагов: {len(enemies)}.")
                        print(f"Бой: {len(rounds)} раундов.")
                    else:
                        print(f"{enemy.capitalize()} оказался сильнее. Вы падаете.")
            case "8":
                # --- Таблица лидеров ---
                print_leaderboard(log)

        # --- Проверка гибели ---
        if health <= 0:
            print(f"{hero_name} падает без сил. Соляные шахты забирают ещё одного искателя.")
            outcome = "гибель"
            running = False

        # --- Счётчик действий ---
        if running:
            actions += 1

        # --- Строка состояния ---
        print()
        print(f"Здоровье: {health:4d}   Запас сил: {stamina:4d}   Врагов осталось: {len(enemies)}")
        print()

except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")

finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")

    print_run_summary(log)
    print(frame)