# Распоковка - извлечение и присвоение их переменным

# Распоковка списков (list) - помнить что список упорядочен порядок важен

my_auto = ['bmw', 'lada', 'tesla']
my_bmw, my_lada, my_tesla = my_auto # распаковка
print(my_bmw, my_lada, my_tesla)
print(my_auto)

# Распоковка кортежей (tuple) 

my_auto = ('bmw', 'lada', 'tesla')
my_bmw, my_lada, my_tesla = my_auto  # распаковка
print(my_bmw, my_lada, my_tesla)
print(my_auto)

# Распоковка словаря  в именннованые аргументы

user = {
	'name': 'Petr',
	'comments_qty': 29
}

def user_info(name, comments_qty=0):
	if not comments_qty:
		return f'{name} нет комментов'
	return f'у {name} {comments_qty} комментов'

print(user_info(**user))


# Распоковка списка в позиуионные аргументы


user = ['Petr', 23]


def user_info(name, comments_qty):
	if not comments_qty:
		return f'{name} нет комментов'
	return f'у {name} {comments_qty} комментов'


print(user_info(*user))
