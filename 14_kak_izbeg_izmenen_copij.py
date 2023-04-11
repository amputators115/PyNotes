# Как избежать изменений копий

# Вариант 1

from copy import deepcopy

info = {
	'name': 'Petr',
	'poffesion': 'driver'
}

info_copy = info.copy()
info_copy['age'] = 24

print(info_copy)
print(info)

print(id(info_copy))
print(id(info))

# Значения вложенных элементов Внимание изменяют исходный объект

info = {
	'name': 'Petr',
	'poffesion': 'driver',
	'age': []
}

info_copy = info.copy()
info_copy['age'].append(34)

print(info_copy)
print(info)

# Глубокое копирование объекта deepcopy


info = {
	'name': 'Petr',
	'poffesion': 'driver',
	'age': []
}

info_copy = deepcopy(info)
info_copy['age'].append(34)

print(info_copy)
print(info)
