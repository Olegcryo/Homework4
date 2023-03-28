# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
n_elements  = set(randint(1, 10) for i in range(int(input('Введите количество эелементов первого множества --> '))))
print(n_elements )
m_elements = set(randint(1, 10) for i in range(int(input('Введите количество элементов второго множества --> '))))
print(m_elements)
numbers = sorted(n_elements .intersection(m_elements))
print(f'Числа , встречающиеся в обоих набора: {numbers}')
