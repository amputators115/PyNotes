# Лямбда функции - всегда анонимны(нет имени)
# lambda парметр, параметр: выражение (только одно)

# обычная функция

def my_fn(a, b):
    c = a * b
    return c


print(my_fn(10, 20))

# Лямбда функция
# не следует присваивать перемеенной иначе будет переформатировано в обычную функцию согласно PEP8

lambda a, b: a * b


def my_lambda_func(a, b): 
	return a * b

print(my_lambda_func(10, 10))

# Где стоит испольщовать лямбда функции?
# В качестве тела внутри обычной функции

def greeting(greet):
	return lambda name: f'{greet}, {name}'

gr_morn = greeting('Добрый вечер') # Присваиваем переменной имя функции
print(gr_morn('Петя'))  # Печатаем переменную в параметр имя

# Моя тачка BMW

def auto(mojatachka):
	return lambda brand: f'{mojatachka} {brand}'

my_auto = auto('Моя тачка')
print(my_auto('BMW'))

# Тоже самое обычной функцией


def auto(mojatachka):
	def tacka(brand):
		return f'{mojatachka} {brand}'
	return tacka


my_auto = auto('Моя тачка')
print(my_auto('BMW'))



