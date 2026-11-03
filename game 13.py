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

# --- Враги, журнал, золото и инвентарь ------------
enemies = ["скелет", "гуль", "паук", "летучая мышь", "соляной голем"]
log = []           
gold_total = 0     
ability_bonus = 0  

# --- Магазин по названию ---------------------------
prices = {
    "зелье": 10,
    "масло для факела": 15,
    "боевой эликсир": 40,
}

# --- Рюкзак ---------------------------------------
inventory = {}

# --- Карточки врагов ------------------------------
enemy_stats = {
    "скелет":        {"hp": 45.0, "damage": 6, "loot": 25},
    "гуль":          {"hp": 30.0, "damage": 4, "loot": 15},
    "паук":          {"hp": 20.0, "damage": 3, "loot": 10},
    "летучая мышь":  {"hp": 12.0, "damage": 2, "loot": 5},
    "соляной голем": {"hp": 60.0, "damage": 8, "loot": 40},
}

# --- КАРТА ПОДЗЕМЕЛЬЯ (5x5) -----------------------
MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "#", "S", ".", "#"],
]

# --- Направления как пары (dr, dc) ----------------
DIRECTIONS = {
    "north": (-1, 0),
    "south": (1, 0),
    "west": (0, -1),
    "east": (0, 1),
}

# --- Лут в комнатах (ключ — кортеж координат) -----
LOOT = {
    (1, 1): "старая монета",
    (2, 3): "пыльное зелье",
    (3, 3): "самоцвет стража",
}
found_loot = set()

# --- Позиция героя и посещённые комнаты -----------
hero_r, hero_c = 4, 2
visited = {(4, 2)}

# --- Словарь-переводчик номеров в глаголы ---------
num_to_verb = {
    "1": "look", "2": "go", "3": "rest", "4": "listen",
    "5": "torch", "6": "train", "7": "descend", "8": "leaders",
    "9": "shop", "10": "backpack", "11": "drink", "0": "exit",
}

# --- Список команд для справки --------------------
commands = [
    "look", "go [north|south|west|east]", "rest", "listen", "torch", "train",
    "descend", "leaders", "shop", "backpack", "drink potion",
    "buy <item> [count]", "map", "scout", "help", "exit",
]

# --- Меню -----------------------------------------
MENU = [
    "Что делаешь? (номер или команда; help — справка)",
    "1 - осмотреться (look)",
    "2 - идти вперёд (go [north|south|west|east])",
    "3 - отдохнуть (rest)",
    "4 - прислушаться (listen)",
    "5 - постучать по стене (torch)",
    "6 - тренировка (train)",
    "7 - спуститься глубже (descend)",
    "8 - таблица лидеров (leaders)",
    "9 - магазин (shop)",
    "10 - рюкзак (backpack)",
    "11 - выпить зелье (drink potion)",
    "0 - выйти из подземелья (exit)",
    "map - карта, scout - обход",
]


# ==================================================
# ФУНКЦИИ ПРАВИЛ
# ==================================================

def hero_hit(strike_n):
    """
    Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные damage и crit_damage, не меняет ничего.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(stats, hero_health, bonus=0):
    """
    Бой с врагом по карточке stats до гибели одного из двоих.
    stats — словарь с ключами hp, damage, loot.
    bonus — надбавка к урону героя, по умолчанию 0.
    Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot):
    таблицу раундов, признак победы, здоровье после боя и добычу.
    """
    enemy_name = stats.get("name", "враг")
    enemy_hp = stats["hp"]
    enemy_damage = stats["damage"]
    rounds = []
    round_n = 0

    print(f"Вы спускаетесь по лестнице. Из темноты появляется {enemy_name}!")

    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit = hit + bonus
        enemy_hp -= hit

        line = f"Раунд {round_n}: вы наносите {hit:.1f} урона"
        if crit:
            line += " — критический!"

        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            hero_health -= enemy_damage
            line += (f" Здоровье {enemy_name}: {enemy_hp:.1f}. "
                     f"{enemy_name.capitalize()} бьёт в ответ на {enemy_damage}.")
            rounds.append([round_n, hit, enemy_damage])

        print(line)

    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """
    Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1.
    Возвращает (gold_left, ok): остаток золота и признак успеха.
    Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(log):
    """
    Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None: контракт функции — печать, а не данные.
    """
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
    """
    Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге не было боёв.")


def scout(r, c, seen):
    """
    Рекурсивно обходит карту от клетки (r, c).
    Возвращает число доступных комнат.
    seen — множество посещённых клеток, общее на весь обход.
    """
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total


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

# --- Потолки здоровья и сил ------------------------
max_health = health
max_stamina = stamina

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
outcome = "прерывание"

try:
    while running:
        print("\n".join(MENU))
        print()

        # --- Чтение и нормализация команды ---
        line = input()
        cmd = line.strip().lower()

        while cmd == "":
            print("Пустая команда. Введи номер или слово (help — справка).")
            line = input()
            cmd = line.strip().lower()

        words = cmd.split()
        verb = words[0]

        # --- Перевод номера в глагол ---
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
            words = [verb]
            cmd = verb

        match verb:
            case "exit":
                print("Вы поднимаетесь обратно к свету. Соляные шахты остаются позади.")
                outcome = "выход"
                running = False

            case "look":
                print("Вы осмотрелись. Стены шахты покрыты белыми разводами соли, "
                      "в углу лежит старая кирка, а на полу — следы чьих-то сапог.")

            case "go":
                # --- Шаг по карте, если указано направление ---
                if len(words) > 1 and words[1] in DIRECTIONS:
                    direction = words[1]
                    dr, dc = DIRECTIONS[direction]
                    nr, nc = hero_r + dr, hero_c + dc

                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))

                        # --- Подбор лута ---
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Вы нашли {item}! Уникального лута: {len(found_loot)}.")

                        print(f"Вы шагаете на {direction}. Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Нельзя идти на {direction}: стена или край карты.")
                else:
                    # --- Прежний коридорный шаг ---
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

            case "rest":
                stamina = min(stamina + 2, max_stamina)
                print("Вы присели у стены и отдохнули. Дыхание выровнялось, "
                      "силы понемногу возвращаются.")

            case "listen":
                print("Вы замерли и прислушались. Где-то в глубине шахты "
                      "капает вода, и слышен тихий скрежет — будто кто-то скребёт камень.")

            case "torch":
                stamina = stamina - 1
                print("Вы постучали по стене. Соль осыпалась, и за ней "
                      "обнаружилась небольшая трещина — но разбить стену голыми руками не выйдет.")

            case "train":
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

                stamina = stamina - 2
                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")

            case "descend":
                if not enemies:
                    print("Вы спускаетесь по лестнице, но подземелье пусто. "
                          "Здесь больше не с кем сражаться.")
                else:
                    enemy = random.choice(enemies)
                    stats = enemy_stats[enemy].copy()
                    stats["name"] = enemy

                    rounds, won, health, loot = fight(stats, health, bonus=ability_bonus)

                    for r in rounds:
                        log.append(r)

                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} побеждён! В подземелье осталось врагов: {len(enemies)}. "
                              f"Добыча: {loot} золота.")
                        print(f"Бой: {len(rounds)} раундов.")
                    else:
                        print(f"{enemy.capitalize()} оказался сильнее. Вы падаете.")

            case "leaders":
                print_leaderboard(log)

            case "shop":
                print("Магазин:")
                for name, price in prices.items():
                    print(f"{name}: {price} золота")

            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")

            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])

                if item == "":
                    print("Купить что? Введи: buy <предмет>.")
                elif item not in prices:
                    print("Такого предмета в магазине нет.")
                else:
                    gold_total, ok = buy(prices[item], gold_total, quantity=qty)
                    if ok:
                        inventory[item] = inventory.get(item, 0) + qty
                        print(f"Куплено {qty} {item} за {prices[item] * qty} золота. "
                              f"Осталось золота: {gold_total}.")
                    else:
                        print(f"Не хватает золота: нужно {prices[item] * qty}, "
                              f"есть {gold_total}.")

            case "drink":
                item = " ".join(words[1:]) or "зелье"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет: {item}.")
                else:
                    health = min(health + 10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Вы выпили {item}. Здоровье: {health}. "
                          f"Осталось: {inventory.get(item, 0)}.")

            case "map":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))

            case "scout":
                seen = set()
                count = scout(hero_r, hero_c, seen)
                print(f"Разведка: доступно комнат — {count}.")

            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0–11 работают как раньше.")

            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введи 'help'.")
                continue

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
        print(f"Здоровье: {health:4d}   Запас сил: {stamina:4d}   "
              f"Врагов осталось: {len(enemies)}   Золото: {gold_total}")
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

    if not inventory:
        print("В рюкзаке ничего не осталось.")
    else:
        print("В рюкзаке осталось:", end=" ")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.", end=" ")
        print()

    if found_loot:
        print("Найден уникальный лут:", ", ".join(found_loot) + ".")
    else:
        print("Уникального лута не найдено.")

    print_run_summary(log)
    print(frame)