# Обработка ошибок
# Try/except

try:
	# блок кода который пытаемся выполнить
	pass
except ErrorType:
	# Этот блок выполняется в случае возникновения оошибки в блоке try
	pass

try:
	print(10 / 0)
except ZeroDivisionError:
	print('Ошибка деления на ноль')

print('Продолжение.......')

# Получение информации об ошибке автоматически возникающей в блоке try

try:
	print(10 / 0)
except ZeroDivisionError as e:
	print(type(e))
	print(dir(e))
	print(e)

print('Продолжение.......')

# Возникновение разных типов ошибок

try:
	print('10' / 0)
except ZeroDivisionError as e:
	print(type(e))
	print(e)

except TypeError as e:
	print(e)
	print(type(e))

print('Продолжение.......')

# Если в блоках не возикло ошибок то выполниться в блоке else

try:
	print(10 / 2)
except ZeroDivisionError as e:
	print(type(e))
	print(e)

except TypeError as e:
	print(e)
	print(type(e))

else:
	print('Ошибок нет')
print('Продолжение.......')

# Возможно использовать конструкцию try/except/else/finally

try:
	print(10 / 2)

except ZeroDivisionError as e:
	print(type(e))
	print(e)

except TypeError as e:
	print(e)
	print(type(e))

else: # выпоняется в любом случае если ошибок не возникло
	print('Ошибок нет')

finally: # Выполняется всегда по умолчанию пример отключение от базы данных 

    print('Продолжение.......') 

# Есть ситуации когда вы не знаете какая ошибка возникнет тогда следует указать класс ошибок Exception - универсальный подход 

try:
	print (10 / 0)

except Exception as e:
	print(e)
	print(type(e))


# Cоздание ошибок
# Генерация ошибки с помощью raise

def my_nums(a,b):
	if b == 0:
		raise TypeError('Здесь ваш текст ошибки')
	return a/b


try:
	my_nums(10,0)

except TypeError as e:
	print(e)
	print(type(e))

else:  # выпоняется в любом случае если ошибок не возникло
	print('Ошибок нет')

