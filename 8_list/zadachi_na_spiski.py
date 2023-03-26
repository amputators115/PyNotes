# Задачи на списки

'''Задача 1'''
# 1. Создайте список с 5 элементами разных типов
my_list = [1, 2.4, 'Vova', True, {'age':24, 'city': 'Msc'}]
# 2. Удалите 3-й элемент
my_list.pop(3)
# 3. Выведите в терминал длину списка
print(len(my_list))
# 4. Поменяйте порядок следования элементов в списке
my_list.reverse()
# 5. Создайте еще один спискок с двумя элементами
my_new_list = [23, 75]
# 6. Расширьте 1-й список элементами 2-го
print(my_list + my_new_list)
# 7. Выведите в терминал ИТОГ : 6 элементов
print(len(my_list + my_new_list))

my_list = [1, 2.4, 'Vova', True, {'age': 24, 'city': 'Msc'}]
my_list.pop(3)
print(len(my_list))
my_list.reverse()
my_new_list = [23, 75]
print(my_list + my_new_list)
print(len(my_list + my_new_list))


'''Задача 2'''

# 1. Создайте 2 списка
my_list = [1, 2.4, 'Vova', True, {'age': 24, 'city': 'Msc'}]

# 2. Объедините 2 списка используя оператор '+'
my_new_list = [23, 75]

# 3. Определите какой магический метод списков вываеться при '+'

print(dir(my_list))
print(help(list.__add__))
# 4. Выполните слияние списков используя магический метод
# 5. Результат вывести в терминал
print(my_list.__add__(my_new_list))

my_list = [1, 2.4, 'Vova', True, {'age': 24, 'city': 'Msc'}]
my_new_list = [23, 75]
print(dir(my_list))
print(help(list.__add__))
print(my_list.__add__(my_new_list))

