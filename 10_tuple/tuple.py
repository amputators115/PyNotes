# Кортежи

# Кортежи это не изменяемые объекты.
# Кортежи изменять нельзя!

my_tuple = ('Volvo', 'BMW', 'Tesla')
new_tuple = ('Tesla', 'BMW', 'Volvo')

print(my_tuple == new_tuple)

# Получение длины кортежа len

my_tuple = ('Volvo', 'BMW', 'Tesla')
print(len(my_tuple))

# Получение элемента кортежа по индексу []

my_tuple = ('Volvo', 'BMW', 'Tesla')
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[-2])

# Ошибка при попытке изменить, удалить значение

my_tuple = ('Volvo', 'BMW', 'Tesla')
my_tuple[-1] = 'Lada'
print(my_tuple)

my_tuple = ('Volvo', 'BMW', 'Tesla')
del my_tuple[0]
print(my_tuple)

# Кортеж словарей(изменяемые объекты) Словари в кортежи изменять можно

user = (
    {
        'user_id': 24,
        'user_name': 'Petr',
    },

    {
        'user_id': 25,
        'user_name': 'Ivan',
    }
)

print(len(user))
print(user[1]['user_id'])
print(user[0]['user_id'])

user[0]['user_id'] = 100
print(user[0]['user_id'])

# В кортежах можно использовать переменные

my_name = 'Petr'
my_age = 24
my_city = 'Msc'

my_tuple = (my_name, my_age, my_city)

print(my_tuple)

# Кортежи можно объединять с поммощью + (__add__)


my_tuple = (23, 567, 89)
my_new_tuple = ('Volvo', 'BMW', 'Tesla')
print(my_tuple + my_new_tuple)

my_tuple = (23, 567, 89)
my_new_tuple = ('Volvo', 'BMW', 'Tesla')
print(my_tuple.__add__(my_new_tuple))
print(type(my_tuple.__add__(my_new_tuple)))
