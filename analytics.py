#!/usr/bin/env python3
"""
Модуль аналитики (ветка dev2)
"""


def average(numbers: list) -> float:
    """Возвращает среднее значение списка"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def max_value(numbers: list):
    """Возвращает максимальное значение"""
    return max(numbers) if numbers else None


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(f"Average: {average(data)}")
    print(f"Max: {max_value(data)}")
# analytics module v1.1
