# Диапозоны - Это упорядочная последовательность элементов

my_range = range(9)
print(my_range)

# Конвертация диапозона в список

my_range = range(9)
print(list(my_range))

# При создании диапозона можно указать начальное значение и конечное

my_range = range(10, 40, 3)
print(my_range)
print(list(my_range))

# У элементов есть индексы

my_range = range(10, 40, 3)
print(list(my_range))
print(my_range[0])
print(my_range[2])

# Цикл для range (итерация для диапозона)

my_range = range(10, 40, 3)
for n in my_range:
	print(n)

for n in range(1, 5, 8):
    print(n)


# Дипозоны можно конвертировать в списки и так далее кроме словарей


print(list(range(1, 5, 8)))
print(set(range(12, 17, 22)))
print((range(12, 17, 22)))

# Методы диапозонов

my_range = range(5)
print(dir(my_range))

# Метод count - есть ли такой элемент в диапозоне

my_range = range(10, 40, 3)
print(my_range.count(10))

my_range = range(10, 40, 3)
print(my_range.count(11))

# Метод index() - индекс элемента

my_range = range(10, 30, 3)
print(my_range.index(19))


