#!/usr/bin/env python3
"""
Главный модуль приложения - изменено в dev3
"""


def greet(name: str) -> str:
    """Возвращает приветствие с восклицательным знаком"""
    return f"Hello, {name}! Welcome!"


def main():
    """Точка входа"""
    print(greet("World"))
    print("Version: dev3")


if __name__ == "__main__":
    main()
