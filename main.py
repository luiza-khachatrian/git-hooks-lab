#!/usr/bin/env python3
"""
Главный модуль приложения - изменено в dev2
"""


def greet(name: str) -> str:
    """Возвращает приветствие"""
    return f"Hello, {name}!"


def main():
    """Точка входа"""
    print(greet("World"))
    print("Author: person2")


if __name__ == "__main__":
    main()
