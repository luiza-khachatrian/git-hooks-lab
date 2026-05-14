#!/usr/bin/env python3
"""
Главный модуль приложения - изменено в dev
"""


def greet(name: str) -> str:
    """Возвращает приветствие"""
    return f"Hello, {name}! Have a great day!"


def main():
    """Точка входа"""
    print(greet("World"))


if __name__ == "__main__":
    main()
