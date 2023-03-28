# Словари

auto = {
	'brand': 'Lexus',
	'year':2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto)
print(type(auto))


# Порядок элементов не имеет значение.Нет индекса. При этом это будут два разных объекта по id


auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

new_auto = {
	'engine': 4.5,
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
	'brand': 'Lexus',
}

print(new_auto == auto)
print(id(auto))
print(id(new_auto))




