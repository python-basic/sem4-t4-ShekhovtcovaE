"""
    Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).
    Шеховцова Е. Г.
"""

import random

list = [random.randint(-100, 100) for i in range(6)]
print(list)

# Разделение положительных/отрицательных чисел
posit = []
negat = []
for i in list:
    (lambda i: posit.append(i) if i>0 else negat.append(i))(i)

print(posit)
print(negat)

# четноых/нечетных чисел
even = []
odd = []
for i in list:
    (lambda i: odd.append(i) if i % 2 else even.append(i))(i)

print(even)
print(odd)
