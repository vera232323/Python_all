# # Задача 1. Создайте файл. Запишите в него N 
# первых элементов последовательности Фибоначчи.
# # 6 –> 1 1 2 3 5 8
def zadacha1():
    count = 12
    num_f = 0
    num_s = 1

    data = open('z1dz3.txt', mode ='w',encoding='utf-8')
    for _ in range(count):
        data.write(str(num_f)+ '\n')
        num_f, num_s = num_s, num_f + num_s

    data.close()
# zadacha1()
# # Задача 2. В файле находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
def zadacha2():
    data = open('z2dz3.txt', encoding='utf-8')
    fruit_list = data.readlines()[0].split(' ')
        # или fruit_list = data.readline()
    data.close()
    print(fruit_list)
    letter = 'к'

    for fruit in fruit_list:
        if fruit[0] == letter:
            print(fruit)

# zadacha2()

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.
def zadacha3():

    def set_phrase_lest():
        data = open('z3dz3.txt', mode='r', encoding='utf-8')
        phrase_list = data.readlines()
        data.close()
        print(phrase_list)
        dictionary = {}
        for phrase in phrase_list:
            phrase=phrase.removeprefix('')
            phrase=phrase.split(': ')
            # removeprefix('') в конце строки убираем 
            # переход на новую строку
            print(phrase) 
            dictionary[phrase[0]]= phrase[1]    
        return dictionary  
    set_phrase_lest()
    phrase_dictionary = set_phrase_lest()

        # или можно просто написать слова : phrase_dictionary = {}
    start_dialog = True
    while start_dialog:
        phrase = input('Я: ')
        phrase = phrase.lower()
        if phrase in phrase_dictionary.keys():
            print(f'Бот: {phrase_dictionary[phrase]}')
        else:
            print(f'Бот: я не знаю, что отвечать...')
            check = input('Бот: хочешь научить меня отвечать? (Y/N)\nЯ: ')
            check = check.lower()
            if check == 'y':
                answer = input(f'Бот: как бы ответил на фразу "{phrase}"?\nЯ: ')
                data = open ('phrase.txt',mode = 'a',encoding='utf=8')
                data.write(f'{phrase}:{answer}\n')
                data.close()
    #             # phrase_dictionary [phrase]= answer
                phrase_dictionary = set_phrase_lest()
        if phrase == 'разговор оконен' or phrase == 'все понятно':
            start_dialog = False
zadacha3()