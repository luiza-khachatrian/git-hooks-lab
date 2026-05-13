#!/usr/bin/env python3
"""
Главный модуль приложения
"""

def greet(name: str) -> str:
    """Возвращает приветствие"""
    return f"Hello, {name}!"


def main():
    """Точка входа"""
    print(greet("World"))


if __name__ == "__main__":
    main()
