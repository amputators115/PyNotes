# Наборы - неупорядочные элементы последовательность роли не играет. Набор содержит только уникальные элементы Изменять наборы можно Нет индексов.

# Cинтаксис

my_set = {'apple', 'ibm', 'dell'}
print(my_set)
print(type(my_set))

# Только уникальные элементы дубликаты будут удалены. Преимущество - найти уникальные значения в не уникальных

my_set = {'apple', 'ibm', 'dell', 'apple'}
print(my_set)
print(type(my_set))

# последовательность роли не играет

my_set = {'apple', 'ibm', 'dell'}
my_set_two = {'ibm', 'dell', 'apple'}

print(my_set == my_set_two)

# Длина набора len

my_set = {'apple', 'ibm', 'dell'}
print(len(my_set))

