"""
Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).
Шеховцова Е. Г.
"""

import random

list = [random.randint(-100, 100) for i in range(6)]
print(list)

posit = []
negat = []
for i in list:
    (lambda i: posit.append(i) if i>0 else negat.append(i))(i)

print(posit)
print(negat)
