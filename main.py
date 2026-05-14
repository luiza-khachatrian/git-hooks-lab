#!/usr/bin/env python3
"""
Главный модуль приложения - merged
"""


def greet(name: str) -> str:
    """Возвращает приветствие с восклицательным знаком"""
    return f"Hello, {name}! Welcome!"


def main():
    """Точка входа"""
    print(greet("World"))
    print("Version: dev3")
    print("Author: person2")


if __name__ == "__main__":
    main()
