# Условыне инструкции - использовать допускается оператор and not or
# if если условие правдиво то блок кода выполняется
# Когда достаточно условий лучше использовать if if if if

my_num = 25

if my_num > 0:
	print('число больше ноля')

# if not с оперратором not

my_dict = {
	'name': 'petr',
	'age': 24,
}

if not my_dict.get('work'):
	print('Не работает')

if my_dict.get('name'):
	print('Но есть другие данные')

# if else

my_num = 31

if type(my_num) is int:
	print('целое число')
else:
	print('не целое число')

my_auto = {
	'price': 2000,
	'brand': 'lada'
}

if my_auto.get('brand'):
	print('Есть название тачки', my_auto['brand'], 'и ценник ей', my_auto['price'])
else:
	print('нет названия тачки')

# if elif else

my_num = -10

if my_num > 0:
	print('>0')
elif my_num < 0:
	print('<0')
else:
	print('тут ноль')





