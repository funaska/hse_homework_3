"""
Напишите функцию calc_factorial, которая вычисляет факториал для любого
неотрицательного целого числа
"""

import sys


def calc_factorial(n):
    """
    вычисляет факториал для любого неотрицательного целого числа

    вход:
    n - неотрицательное целое число

    выход:
    result - факториал от входного числа, int
    """

    result = 1
    if(n < 0):
        sys.exit('Входное число меньше ноля!')
    else:
        result = 1
        for i in (range(1, n+1)):
            result *= i
    return result

if __name__ == '__main__':
    print(calc_factorial(5))
