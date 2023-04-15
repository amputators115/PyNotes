# Оператор распоковки словаря **

button = {
	'width': 200,
	'text': 'buy'
}

red_button ={
	**button, # Распоковка словаря.
	'color': 'red'
}

print(red_button)
print(button)

# Порядок важен ** ниже не перзапишет цвет 

button_grey = {
	'width': 200,
	'text': 'buy',
	'color': 'grey'
}

red_button = {
	'color': 'red',
	**button_grey,  # Распоковка словаря.
}

print(red_button)
print(button_grey)

# Объединение словарей с помощью опертора распоковки словаря

button_info = {
	'text': 'buy',
}

button_style = {
	'color': 'red',
	'width': 200,
	'heigt': 300,
}

button = {
	**button_info,
	**button_style,
}

print(button)

# Более простой спосооб объединение слвоарей через |

button_info = {
	'text': 'buy',
}

button_style = {
	'color': 'red',
	'width': 200,
	'heigt': 300,
}

button = button_style | button_info

print(button)
