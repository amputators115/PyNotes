# Функции - блок кода который можно выполнять многократно

def sum(a, b):
    c = a + b
    print(c)


sum(2, 2)


def sum(a, b):
    c = a + b
    return c


res = sum(2, 2)
print(res)

# Функция это объект


def sum(a, b):
    c = a + b
    print(c)


print(type(sum))
print(dir(sum))

# Функция возвращает Nan - если нет return
# Функция прекрает свою работу только после возвращение результата (return)
# Параметры, return, аргументы - опционально можно не передавать


def sum(a, b):
    c = a + b


sum(1, 1)

# Самая короткая функция (pass - когда вы не знаете что будет в теле функции)


def sum():
    pass


print(sum())

# Внутри функции не рекомендуется изменять внешние объекты
# Лучше всего копировать .copy() внутри функции


def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Petr',
    'age': 24
}

new_person = increase_person_age(person_one)
print(new_person['age'])
print(person_one['age'])

# Может ли функция иметь любое количество аргументов?
# Да может когда объедянеется в кортеж аругментов

# Объединение элементов в tuple - кортеж оператор *


def sum_nums(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)


print(sum_nums(2, 3, 7))

# Позиционные аргументы (порядок следования важен)


def post_info(name, post):
    info = f'{name} wrote {post}'
    return info


info = post_info('Petr', 45)
print(info)

# Аргументы с ключевыми словами - код более читаем


def post_info(name, post):
    info = f'{name} wrote {post}'
    return info


info = post_info(name='Petr', post=45)
print(info)

# Объединение позиционных аргументов в словарь(dict) оператор **

def post_info(**person):
	
    info = (
		f"{person['name']} wrote " 
		f"{person['post']} post"
	)
    return info

info = post_info(name='Petr', post=45)
print(info)

