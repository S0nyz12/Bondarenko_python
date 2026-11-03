# Lib3 (выполнить в терминале)
python -m venv .venv
.venv\Scripts\activate
pip install colorama
pip freeze > requirements.txt

# Lib3 (.gitignore)
.venv/
__pycache__/
*.save

# Lib4 
try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

# Lib4 
state = f"Health: {health} Stamina: {stamina} Enemies left: {len(enemies)} Gold: {gold_total}"
if COLOR:
    print(Fore.GREEN + state + Style.RESET_ALL)
else:
    print(state)

# Lib5 (комментарий с найденными константами)
# Дополнительные цвета: Fore.BLUE, Fore.MAGENTA, Fore.CYAN
# Дополнительные стили: Style.BRIGHT, Style.DIM

# Lib5 (пример покраски строки победы)
win_msg = f"{enemy.capitalize()} defeated! {len(enemies)} enemies left in the dungeon."
if COLOR:
    print(Fore.CYAN + win_msg + Style.RESET_ALL)
else:
    print(win_msg)

# Lib6 
"""Модуль правил подземелья: бой, магазин, характеристики врагов.

Содержит функции для расчёта урона, проведения боя и покупок, 
а также словари с ценами и статами врагов.
"""
import random