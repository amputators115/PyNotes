# Методы наборов

# .add - добавление в набор

my_set = {'1920x1080', '1080x720'}
my_set.add('720x640')

print(my_set)

# .union - объединение наборов(объединение множеств с удалением дублей)

my_set = {'1920x1080', '1080x720'}
my_other_set = {'640x200', '1080x1080'}
new_set = my_set.union(my_other_set)
print(new_set)

# | - оператор который выполнит так же объединение 2-х наборов

my_set = {'1920x1080', '1080x720'}
my_other_set = {'640x200', '1080x1080'}
new_set = my_set | my_other_set
print(new_set)

# .intersection - пересечение наборов что является общим в двух и более наборов

my_set = {'1920x1080', '1080x720'}
my_other_set = {'1080x720', '1080x1080'}
new_set = my_set.intersection(my_other_set)
print(new_set)

# & - так же пересечение наборов что является общим в двух и более наборов

my_set = {'1920x1080', '1080x720'}
my_other_set = {'1080x720', '1080x1080'}
new_set = my_set & my_other_set
print(new_set)

# .issubset - проверяет включенли один наюор в другой. Более детально следует изучить теорию множеств

my_set = {10, 5, 45}
my_other_set = {10, 5, 45, 678}
new_set = my_set.issubset(my_other_set)
print(new_set)

# discard - удаляет один из элементов

my_set = {10, 5, 45}
my_other_set = {10, 5, 45, 678}
print(my_set.discard(45))
print(my_set)

# remove - удаляет один из элементов

my_set = {10, 5, 45}
my_other_set = {10, 5, 45, 678}
print(my_set.remove(45))
print(my_set)

# copy - копирование
