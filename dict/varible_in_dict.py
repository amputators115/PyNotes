# Использование переменных в коде

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto)

new_brand_dict = 'brand'
auto[new_brand_dict] = 'Honda'
print(auto)

# Вложенные словари

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
	'price_info': {
		'price': 25000,
		'is_avaible': True
	}
}

print(auto)

# Обращение и вывод вложенного словаря

print(auto['price_info'])

# Обращение и вывод значения ключа

print(auto['price_info']['price'])

# Удаление элемента в во вложенном словаре

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
	'price_info': {
		'price': 25000,
		'is_avaible': True
	}
}

print(auto)

del auto['price_info']['is_avaible']
print(auto)

# Удаление вложенного словаря


auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
	'price_info': {
		'price': 25000,
		'is_avaible': True
	}
}

print(auto)

del auto['price_info']
print(auto)

# Создание словаря из переменных

brand = 'Lexus'
year = 2022
color ='red'
engine= 4.5

auto = {
    'brand': brand,
    'year': year,
    'color': color,
    'engine': engine
}

print(auto)

