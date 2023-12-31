# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
if a < b + c and b < a + c and c < a + b:
    print("Треугольник существует! ")
 
    if a == b == c:
        print("И он равносторонний! ")
    if a == b and b != c or b == c and c != a or c == a and a != b:
        print("И он равнобедренный! ")
    if a != b and b != c and c != a:  
        print("И он разносторонний! ")
else:
    print("Треугольник не существует! ")

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input("Введите число от 1 до 100000: "))
while a <= 0 or a > 100000:
    print("AAA! Введите корректное число!")
    exit()
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число является простым")
else:
    print("Число является составным")


# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

import random
number=(random.randint(0, 1000))

a = 1000
b = 0
COUNT_TRY = 10
print(f"Угадай случайное число от {b} до {a}. Угадываем:")
while True:
    try:
        c = int(input())
        c = abs(c)
        if c != number:
            if c > number: 
                a=c
            else:
                b=c
            print(f"Неправильно, число находится в промежутке от {b} до {a}. Попробуй еще раз.")
                                                        
        else:          
            print("Ты угадал, поздравляю!")
            break
    except:
        print(f'Ошибка, вводи только целые числа.')        
        continue

# Нарисовать в консоли ёлку, спросив у пользователя количество рядов.

rows = int(input("Сколько рядов у ёлки? "))
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

MIN = 2
MAX_1 = 9
MAX_2 = 10
for i in range(MIN, MAX_1 + 1):
    for j in range(MIN, MAX_2 + 1):
        print(f'{i} x {j} = {i * j}')
    print(' ')
