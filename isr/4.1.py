"""
     Создание программы по заполнению массивов случайными значениями. 
     Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.
    Шеховцова Е. Г.
"""
import random

list = [round(random.random() * 10) for i in range(6)]
print('До сортировки: ', list)

# Сортировка вставками
def insertSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

list1 = insertSort(list.copy())
print(list1)

# Сортировка пузырьком
def bubbleSort(lst):  
    length = len(lst)
    for j in range(length - 1):
        flag = True
        for i in range(length - j -1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = False
    return lst

print('До сортировки: ', list)
list2 = bubbleSort(list.copy())
print(list2)

# Сортировка с помощью встроенной функции
list3 = sorted(list)
print('До сортировки: ', list)
print(list3)
