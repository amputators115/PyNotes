# Методы кортежей

my_tuple = (23, 567, 89)
print(dir(my_tuple))

# .count -количество раз вречается элемент

my_tuple = (23, 567, 89)
print(my_tuple.count(567))

# .index - индекс опрделенного элемента

my_tuple = (23, 567, 89)
print(my_tuple.index(23))

# Конвертация кортежа в список

my_tuple = (23, 567, 89)
new_my_tuple = list(my_tuple)
print(new_my_tuple)
print(type(new_my_tuple))

# Конвертация списка в кортеж

my_list = [23, 567, 89]
new_my_list = tuple(my_list)
print(new_my_list)
print(type(new_my_list))
