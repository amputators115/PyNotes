# Изменение и удаление значений в словарях

# Получение значений ключа в словарях посредством ['Ключ']

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto['brand'])
print(auto['color'])

# Изменение значений в словарях путем присваивания =


auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

auto['brand'] = 'Lada'
auto['color'] = 'blue'

print(auto['brand'])
print(auto['color'])
print(auto)

# Добавление значений ключа и значения в словари

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

auto['price'] = 5000

print(auto)

# Удаление элементов 


auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

del auto['color']
print(auto)

