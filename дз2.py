# Задача 1. Напишите программу, которая принимает на вход число 
# N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def zadacha1():
    n = int(input('Введите число: '))
    list = [1]

    for i in range (1,n):
        list.append ((i+1) * list [i-1])

    print(list)
zadacha1()

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
# or - коньюнкция
# and - дисьюнкция
def zadacha2():
    print(f'x|y ¬(x v y) v z')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f'{x}|{y}|{int((not x and y) and z)}')
# zadacha2()
# Задача 3. Даны две строки. Посчитайте сколько раз 
# каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def zadacha3():
    firsph='кошки и собаки'
    secondph='собаки и кошки'
    used=[]
    for el in firsph:
        if el not in used:
            used.append(el)
            count = 0
            print(f'Буква{el} втречается {secondph.count(el)}раз(-a)')
# zadacha3()

# Задача 4. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def zadacha4():
    n=8
    num=[]
    for index in range (-n,n+1):
        num.append(index)
    result = num[-2:]+num[:-2]
    print(result)
# zadacha4()