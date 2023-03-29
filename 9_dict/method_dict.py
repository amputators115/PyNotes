# Методы словарей

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto.__doc__)
print(dir(auto))

# items() - возращает список в котором Кортежи

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto.items())

# keys() - возращает ключи словаря

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}
print(auto.keys())
print(list(auto.keys()))  #возвращает список

# popitem() - возращает Кортеж

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}
print(auto.popitem()) # Удаляет последний  элемент ИСПОЛЬЗОВАТЬ НЕ РЕКОМЕНДУЕТСЯ!
print(auto)

# copy() - копирует словарь

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto)
print(id(auto))

new_auto = auto.copy()
print(new_auto)
print(id(new_auto))



