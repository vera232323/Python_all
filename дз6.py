import random
# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396
def zadacha1():

    n=input('введие число: ')
    print(int(n*3)+int(n*2)+int(n))
# zadacha1()    

# Задача 2. Задан массив из случайных 
# цифр на 15 элементов. На вход подаётся 
# трёхзначное натуральное число. Напишите программу,
#  которая определяет, есть в массиве последовательность из трёх элементов,
#  совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
def zadacha2():
    n = [random.randint(0,9) for _ in range(15)]
    print(n)
    num=int(input('введие число: '))
    result=''
    for el in n:
        result+= str(el)
    print(result)

    if str(num) in result:
        print('число есть')
    else:
        print('совпадений нет')
# zadacha2()


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1,
#  знаменатель которых не превышает 11.
def check_n(x,y):
    min_n = min(x,y)
    divider=1
    for el in range(2,min_n+1):
        if x % el == 0 and y % el == 0:
            divider = el
            break
    return divider == 1

def zadacha3():
    for y in range(1,12):
        for x in range(1,y):
            if check_n(x,y):
                print(f'{x}/{y}',end='') 
        print()
zadacha3()