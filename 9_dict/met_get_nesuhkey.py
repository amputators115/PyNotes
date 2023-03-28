# Несуществующие ключи

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}

print(auto['price'])  #KeyError: 'price'

# Get - метод для получения значений ключей

auto = {
	'brand': 'Lexus',
	'year': 2022,
	'color': 'red',
	'engine': 4.5,
}
print(auto.get('price'))  # Значение None - такого ключа нет
print(auto.get('price', False))  # Значение False - такого ключа нет возвратит False
print(auto.get('price', 0)) # Значение 0 такого ключа нет
print(auto.get('brand')) # Ключ есть возратит его значение

