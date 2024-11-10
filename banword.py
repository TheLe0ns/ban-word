import sys
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

# Функция для создания градиента
def gradient_text(text):
    colors = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
    ]
    
    result = ""
    color_count = len(colors)
    for i, char in enumerate(text):
        color = colors[i % color_count]
        result += f"{color}{char}"
    
    return result + Style.RESET_ALL

# Логотип
logo_lines = [
    "▄▄▄▄    ▄▄▄       ███▄    █  █     █░ ▒█████   ██▀███  ▓█████▄ ",
    "▓█████▄ ▒████▄     ██ ▀█   █ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌",
    "▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌",
    "▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌",
    "░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ",
    "░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ",
    "▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ",
    " ░    ░   ░   ▒      ░   ░ ░   ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░ ",
    " ░            ░  ░         ░     ░        ░ ░     ░        ░    ",
    "      ░                                                  ░      "
]

# Функция для печати логотипа с градиентом
def print_gradient_logo(logo):
    for line in logo:
        print(gradient_text(line))  # Печатаем логотип с градиентом

# Функция для замены символов
def replace_characters(text):
    replacements = {
        'п': 'n',
        'е': '3',
        'т': 't',
        'и': 'u',
        'о': '0',
        'ч': '4',
        'б': '6',
        'в': 'B',
        'ы': 'bI',
        'ь': 'b',
        'а': '@',
        'к': 'k',  # Добавлено
        'ш': 'w'   # Добавлено
    }
    
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)  # Заменяем символы
    return text

# Функция для отображения текста
def display_text(text):
    print(text)  # Просто выводим текст

# Основной код
if __name__ == "__main__":
    print_gradient_logo(logo_lines)  # Печатаем логотип с градиентом
    while True:
        try:
            input_text = input("Введите текст: ")  # Запрашиваем ввод текста у пользователя
            modified_text = replace_characters(input_text)  # Заменяем символы
            display_text(modified_text)  # Печатаем измененный текст
        except KeyboardInterrupt:
            print("\nГенерация остановлена.")
            break
