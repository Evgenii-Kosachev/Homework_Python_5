''' Задача: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
    Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
from random import randint

def RandomNaturalCoefficient():
    numb = randint(0, 100)
    return numb

def FormingString(k):
    res = f'{RandomNaturalCoefficient()}*x**{k} + {RandomNaturalCoefficient()}*x + 5 = 0'
    return res

userNumber = input('Set the natural power of the number: ')

with open('Task 1\Data.txt', 'w') as data:
    data.write(f'List of coefficients of a polynomial of degree {userNumber}:\n')
    for i in range(10):
        data.write(f'{FormingString(userNumber)}\n')