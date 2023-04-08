# .symmetric_difference() Симитричная разница в наборах. Поиск элентов кторые есть в наборах но не находятся в пересечениях. Объединение 2-х множеств - персечение

my_set = {'apple', 'ibm', 'dell', 'amd'}
my_set_two = {'apple', 'ibm', 'dell', 'intel'}

print(my_set.symmetric_difference(my_set_two))

# Объединение 2-х множеств - персечение Это равносильно .symmetric_difference

a = {'apple', 'ibm', 'dell', 'amd'}
b = {'apple', 'ibm', 'dell', 'intel'}

print((a | b) - (a & b))


