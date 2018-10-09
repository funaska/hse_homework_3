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
        result = int()
        for i in (range(n)+1):