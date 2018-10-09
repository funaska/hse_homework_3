"""
Напишите функцию для нахождения максимума из 3-х аргументов.
Не пользуйтесь втроенными функциям Питона
"""

def maximum(one, two, three):
    result = one
    # print(result)
    for current in [two, three]:
        # print(current)
        if current > result:
            result = current

    return result


if __name__ == '__main__':
    print(maximum(87, 4, 5))
