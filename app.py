#!/usr/bin/env python3
"""
Hello World приложение для демонстрации композиционного анализа ПО
Использует внешние библиотеки: requests, click, colorama
"""

import sys
import platform
import requests
from click import echo, style
from colorama import init, Fore, Back, Style

# Инициализация colorama для кросс-платформенной работы с цветами
init()


def get_python_version():
    """Получить версию Python"""
    return sys.version


def get_system_info():
    """Получить информацию о системе"""
    return {
        'platform': platform.system(),
        'platform_version': platform.version(),
        'python_version': platform.python_version(),
        'architecture': platform.machine()
    }


def fetch_external_data():
    """Получить данные из внешнего API с использованием requests"""
    try:
        # Используем JSONPlaceholder API для демонстрации
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Ошибка при получении данных: {e}"


def display_hello_world():
    """Отобразить приветственное сообщение с использованием colorama"""
    print(Fore.CYAN + "=" * 50)
    print(Back.WHITE + Fore.BLACK + "  COMPOSITIONAL ANALYSIS DEMO  " + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 50)
    print()


def display_version_info():
    """Отобразить информацию о версиях зависимостей"""
    print(Fore.YELLOW + "Информация о зависимостях:" + Style.RESET_ALL)
    print(Fore.GREEN + f"Python: {get_python_version()}" + Style.RESET_ALL)
    
    # Получаем версии установленных пакетов
    try:
        import click
        import requests
        import colorama
        
        print(Fore.GREEN + f"Click: {click.__version__}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Requests: {requests.__version__}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Colorama: {colorama.__version__}" + Style.RESET_ALL)
    except ImportError as e:
        print(Fore.RED + f"Ошибка импорта: {e}" + Style.RESET_ALL)


def display_system_info():
    """Отобразить информацию о системе"""
    print(Fore.YELLOW + "\nИнформация о системе:" + Style.RESET_ALL)
    info = get_system_info()
    for key, value in info.items():
        print(Fore.WHITE + f"  {key}: {value}" + Style.RESET_ALL)


def display_external_data():
    """Отобразить данные из внешнего API"""
    print(Fore.YELLOW + "\nДанные из внешнего API:" + Style.RESET_ALL)
    data = fetch_external_data()
    
    if isinstance(data, dict):
        print(Fore.WHITE + f"  ID: {data.get('id', 'N/A')}" + Style.RESET_ALL)
        print(Fore.WHITE + f"  Title: {data.get('title', 'N/A')}" + Style.RESET_ALL)
        print(Fore.WHITE + f"  Body: {data.get('body', 'N/A')[:100]}..." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"  {data}" + Style.RESET_ALL)


def main():
    """Главная функция приложения"""
    try:
        # Отображаем приветственное сообщение
        display_hello_world()
        
        # Отображаем информацию о версиях
        display_version_info()
        
        # Отображаем информацию о системе
        display_system_info()
        
        # Отображаем данные из внешнего API
        display_external_data()
        
        print(Fore.CYAN + "\n" + "=" * 50)
        print(Style.BRIGHT + Fore.GREEN + "  Анализ компонентов успешно завершен!  " + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 50)
        print()
        
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nПрограмма прервана пользователем" + Style.RESET_ALL)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\nПроизошла ошибка: {e}" + Style.RESET_ALL)
        sys.exit(1)


if __name__ == "__main__":
    main()