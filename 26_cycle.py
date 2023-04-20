# Циклы (2 типа for in  и while) - можно осуществлять перебор послежовательностей словари, кортежи, и т/д


# Цикл for in для списков

my_list = [1, 3, 7]

for elem in my_list:
	print(elem)

# Цикл for in для кортежей

my_tuple = ('1920x1080', 6 , 'petr')
for elem in my_tuple:
	print(elem)

# Цикл for in для словарей

my_dict = {
	'name': 'petr',
	'age': 27,
}

for elem in my_dict:
	print(elem)
	print(elem, my_dict[elem])
	print(my_dict[elem])


# Цикл for in для словарей при этом доступ сразу и ключ и значение с помощью метода items()

my_dict = {
	'name': 'petr',
	'age': 27,
}

for items in my_dict.items():
	key, value = items
	print(key, value)

# Цикл for in для наборов set

my_set = {'apple', 'ibm', 'dell'}

for el in my_set:
	print(el)


# Цикл for in для строк

my_name = 'Petr'

for a in my_name:
	print(a)

# Цикл for in для диапозонов

for a in range(5):
	print(a)



