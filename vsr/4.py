import random

list1 = [round(random.random() * 10) for i in range(6)]
print('До сортировки: ', list1)

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

print('После сортировки', insertSort(list1))
