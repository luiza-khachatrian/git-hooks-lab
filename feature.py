#!/usr/bin/env python3
"""
Новая функциональность (ветка dev)
"""


def new_feature(data: list) -> list:
    """Удваивает каждый элемент списка"""
    return [x * 2 for x in data]


# Тест функции
if __name__ == "__main__":
    print(new_feature([1, 2, 3, 4]))
