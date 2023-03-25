# Список - это упорядоченная последовательность элементов

my_gadget = ['apple', 'iphone', 'hp']
my_num = [1, 56, 78, 678, 876.8]
user_data = ['petr', 34, '🔴', 'bmw']

# Списки это последовательность элементов у каждого есть индекс

my_gadget = ['apple', 'iphone', 'hp']
new_gadget = ['iphone', 'apple', 'hp']

print(my_gadget == new_gadget)

# Длина списка len

my_gadget = ['apple', 'iphone', 'hp']
print(len(my_gadget))

my_num = [1, 56, 78, 678, 876.8]
print(len(my_num))

user_data = ['petr', 34, '🔴', 'bmw']
print(len(user_data))

# Получение элемента списка по его индексу [число]

my_num = [1, 56, 78, 678, 876.8]
print(my_num[3])
print(my_num[-1])  # Получение последнего элемента в списке
print(my_num[-2])  # Получение предпоследнего элемента в списке
print(my_num[1:3])  # Получение диапозона
print(my_num[2:])
print(my_num[:4])

# Изменение значений в списке по индексу путем присваивания переменная списка [индекс] = значение

my_num = [1, 56, 78, 678, 876.8]
print(my_num)

my_num[0] = 23
print(my_num)

# Изменение нескольких значений в списке

my_num = [1, 56, 78, 678, 876.8]
print(my_num)

my_num[0:3] = 23, 0.5
print(my_num)

# Удаление элемента  из списка

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(len(my_num))

del my_num[-1]
print(my_num)
print(len(my_num))

# Удаление нескольких элемента  из списка

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(len(my_num))

del my_num[1:3]
print(my_num)
print(len(my_num))

# Список может содержать словари('ключ': значение)

users = [
    {
        'user_id': 76,
        'user_name': 'Ivan'
    },
    {
        'user_id': 78,
        'user_name': 'Sergey'
    }
]

print(users)
print(len(users))
print(users[0])
# Добираемся до словаря, следом ключ элемента в словаре
print(users[0]['user_name'])

# Формирование списка из объявленных перменных

my_name, age, city = 'Ivan', 23, 'Mscw'
print(my_name, age, city)

my_list = [my_name, age, city]
print(my_list)

# Обращение по не сущетсвуюещему индексу вдет к ОШИБКЕ
# IndexError: list index out of range

my_num = [1, 56, 78, 678, 876.8]
print(my_num[10])

