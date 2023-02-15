import matplotlib.pyplot as plt 
import numpy as np
# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# # По графику определите, при каких значения x значение функции отрицательно.
def zadacha1():
    '''
    Итоговое задание з 1

    '''
    x_list=[]
    y_list=[]

    for x in range(-10,11):
        y= 5 * x * x + 10 * x - 30
        x_list.append(x)
        y_list.append(y)
    
    plt.axhline(y=0, color ='r', linestyle ='dotted')
    plt.show()
# zadacha1()
def zadacha2():
    size=15
    houses = np.random.randint(100,300, size)
    prices = np.random.randint(3000000,20000000,size)
    mean_pr=[round(prices[i]) for i in range(len(prices))]
    print(mean_pr)
    h_names=['дом 1',
             'дом 2',
             'дом 3',
             'дом 4',
             'дом 5',
             'дом 6',
             'дом 7',
             'дом 8',
             'дом 9',
             'дом 10',
             'дом 11',
             'дом 12',
             'дом 13',
             'дом 14',
             'дом 15']
    plt.axhline(y=5000,color = 'b', linestyle = '--')
    plt.plot(mean_pr,'ro')
    plt.show()
zadacha2() 