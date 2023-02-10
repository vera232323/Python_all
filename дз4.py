from math import pi
import random
# Задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def Zadacha1():
    number = int(input())
    issuccess = True
    list = []
    temp = number

    while issuccess == True:
        for i in range(2, number + 1):
            if number % i == 0:
                list.append(i)
                number = int(number / i)
                issuccess = False
    print(f'{temp} => {list}')

# Zadacha1()
# Задача 2. В первой строке файла находится информация 
# об ассортименте мороженного, во второй - информация о том,
#  какое мороженное есть на складе. Выведите названия того товара,
#  который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»



def Zadacha2():
    with open('z2dz4.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    sentence1 = set(data[0].split(','))
    sentence2 = set(data[1].split(','))
    info = ''
    if len(sentence1) < len(sentence2):
        info = sentence1.difference(sentence2)
    else:
        info = sentence2.difference(sentence1)
    return print(info)
# Zadacha2()
# Задача 3. Выведите число π с заданной точностью.
#  Точность выводится в виде десятичной дроби.
# 3 -> 3.142
def Zadacha3():
    number = int(input())
    print(f"{number} => {round(pi, number)}")
# Zadacha3()

# Задача 4*. Даны два файла, в каждом из которых
#  находится запись многочлена. 
# Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8

def Zadacha4():
    def readfile(filename):
        with open(filename, "r") as f:
            data = f.readlines()
            return data
    string1=readfile('file1.txt')
    string2=readfile('file2.txt')

    def sq_mn(k):
        if 'x^' in k:
            i = k.find('^')
            num = int(k[i + 1:])
        elif ('x' in k) and ('^' not in k):
            num = 1
        else:
            num = -1
        return num
    def k_mn(k):
        if 'x' in k:
            i = k.find('x')
            num = int(k[:i])
        return num


    def calc_mn(st):
        st = st[0].replace(' ', '').split('=')
        st = st[0].split('+')
        lst = []
        l = len(st)
        k = 0
        if sq_mn(st[-1]) == -1:
            lst.append(int(st[-1]))
            l -= 1
            k = 1
        i = 1  # степень
        ii = l - 1  # индекс
        while ii >= 0:
            if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
                lst.append(k_mn(st[ii]))
                ii -= 1
                i += 1
            else:
                lst.append(0)
                i += 1

        return lst
    
    list1=calc_mn(string1)
    list2=calc_mn(string2)
    listlength=len(list1)

    if len(list1)>len(list2):
        listlength=len(list2)
    listnew=[list1[i]+list2[i] for i in range(listlength)]
    if len(list1)>len(list2):
        mm=len(list1)
        for i in range(listlength,mm):
            listnew.append(list1[i])
    else:
        mm=len(list2)
        for i in range(listlength,mm):
            listnew.append(list2[i])
    print(listnew)

# Zadacha4()