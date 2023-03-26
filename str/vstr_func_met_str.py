# Встроенные функции строк

# 1. len() Эта функция используется для вычисления длины последовательности или итерируемого объекта.

print(len('Petr'))

# 2. [число] - получение символа строки по индексу

my_name = 'Petr'
print(my_name[2])
print(my_name[-1])  # Последний символ в строке
print(my_name[-2])  # Предпоследний символ в строке

# 3. [число:число] - диапозон символов в строке

my_name = 'Petr'
print(my_name[0:3])
print(my_name[1:])  # от номер индекса до конца строки
print(my_name[:3])  # до  индекса номер 3 включительно

# Методы строк

# 1. .upper() - вся строка в верхнем регистре

my_name = 'Petr'
print(my_name.upper())

# 2. .replace - замена в строке

my_comment = 'Это была длинная позиция'
print(my_comment.replace('длинная', 'короткая'))

# 3. .count() - количество('символ, 'слов', ' ') в строке

my_comment = 'Это была длинная позиция'
print(my_comment.count('длинная'))
print(my_comment.count(' '))
print(my_comment.count('н'))

# 4. .index() - определение индекса в строка

my_comment = 'Это была длинная позиция'
print(my_comment.index('я'))

# 5. .capitalize() - строка с заглавной

my_name = 'petr'
print(my_name.capitalize())

# 6. .lower() вся строка в нижнем регистре

my_name = 'Petr'
print(my_name.lower())


