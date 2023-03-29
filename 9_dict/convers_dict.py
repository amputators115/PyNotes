# Конвертация других значений в словарь
# Должна быть эмуляция ключ значение

# Конвертация из строки - ошибка

my_list = 'abcd'
new_dict = dict(my_list)
print(new_dict)

# Конвертация из списка - ошибка

my_list = [4, 'abc', True]
new_dict = dict(my_list)
print(new_dict)

# Конвертация из списка списка

my_list = [['age', 35], ['city', 'Msc']]
new_dict = dict(my_list)
print(new_dict)

# Конвертация из списка кортежей 

my_list = [('age', 35), ('city', 'Msc')]
new_dict = dict(my_list)
print(new_dict)

