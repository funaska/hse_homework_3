# hse_homework_3
03_functions_iterators_generators_homework from https://github.com/SlinkoIgor/data_mining_course2

Задание:

1 (1 балла)
Напишите функцию calc_factorial, которая вычисляет факториал для любого неотрицательного целого числа.


2 (1 балл)
Напишите функцию для нахождения максимума из 3-х аргументов. Не пользуйтесь втроенными функциям Питона


3 (3 балла)
Напишите функцию get_factorial_generator, создающую генератор для вывода последовательности из факториалов целых чисел. Дополните уже существующий код:

In [ ]:
def get_factorial_generator():
    # Ваш код здесь
    
factorial_generator = get_factorial_generator()
print(next(factorial_generator))  # печатает 1
print(next(factorial_generator))  # печатает 1
print(next(factorial_generator))  # печатает 2
print(next(factorial_generator))  # печатает 6
print(next(factorial_generator))  # печатает 24
PS: избегайте полного вычисления факториала на каждой итерации


4 (2 + 1 балл)
4.1 Используя функцию calc_factorial из первого задания, напишите list comprehension, который из списка чисел получает список факториалов.

Пример:

[1, 5, 20, 3, 7] -> [1, 120, 2432902008176640000, 6, 5040]

4.2 Не изменяя список, модифицируйте list comprehension, чтобы он пропускал числа больше 30: Пример:

[1, 5, 20, 31, 3, 7] -> [1, 120, 2432902008176640000, 6, 5040]


5 (3 балла)
Функция open(file_name) имеет опциональный аргумент encoding, в который можно передать строкой название кодировки, в которой стоит открыть файл. Большинство файлов в интернете закодированно в 'utf8', но Windows для файлов, в которых содержится кириллица, использует кодировку 'windows-1251'.

Скачайте файлы со стрихотворением Пушкина в разных кодировках: https://raw.githubusercontent.com/SlinkoIgor/data_mining_course2/master/03_functions_iterators_generators/Onegin_utf8.txt и https://raw.githubusercontent.com/SlinkoIgor/data_mining_course2/master/03_functions_iterators_generators/Onegin_windows1251.txt

(скачивать нужно не копируя текст, а файл целиком. Это можно сделать, нажав правой кнопкой на страницу -> сохранить страницу)

Откройте каждый из файлов в питоне, воспользовавшишь функций open(file_name, encoding='utf8') либо open(file_name, encoding='windows-1251') соответственно. Сделайте read и удостоверьтесь, что содержимое файлов полностью совпадает.
