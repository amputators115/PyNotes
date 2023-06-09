# Операторы в Python

# Присвоение
# Арифметические: + - * /, %, //, **, ^
# Сравнения ==, !=, >, <, <=, >= Результатом будет True или False
# Логические not, and, or часто используются в условных конструкциях if else
# Текстовые операторы not, and, or, is, is not, in, not in

# Пример использования опертора is при опрделнии сопадают ли ссылки на объект

a = 10
b = a

c = a + b

print(a is b)
print(a is c)

# У операторов есть магические методы
# К примеру оператор == - 	__eq__()

a = [1, 2]
b = [1, 2]

print(a == b)  # True потому что списки одинаковы
print(a.__eq__(b))
print(a.__eq__)  # Область памяти
print(id(a))
print(hex(id(a)))  # Область памяти  в 16-тиричной кодировке
print(a is b)  # не равны та как занимают разные облатси памяти

# Функция dir() - выводит список имен, атрибутов, методов определенного объекта

print(dir(list))

# Бинарные и унарные операторы

# Унарные операторы состоят из одного операнда

my_num = 10
print(+my_num)  # показываем что здесь число

my_num = 10
print(not my_num)  # отрицание

# Бинарные операторы  два операнда

a = 5
a + b
a += 1  # увеличение на опрделенное число и присовение новго значения перменной
a == b
a and b

# Инфиксная запись - оператор находиться между операторами

a = 5
a + b
a += 1  # увеличение на опрделенное число и присовение новго значения перменной
a == b
a or b
a > b

# Операторы in, not in

# Оператор in - можем проверить есть ли в ловаре название ключа

my_car = {
    'brand': 'bmw',
    'price': 10000
}

print('brand' in my_car)
print('year' in my_car)

# Оператор not in - вариант отрицания

my_car = {
    'brand': 'bmw',
    'price': 10000
}

print('brand' not in my_car)
print('year' not in my_car)

# Логические операторы
# Все пустые значения в типах данных являются False

# Логический оператор not(НЕ) всегда возращает тип bool. Чаще всего используется в интрукциях if. Можно использовать двойное отрицание not not

print(not 10)
print(not not 10)

print(not '')
print(not not '')

my_list = []
print(not my_list)

# Логический оператор and(И) оператор короткокого замыкания

# Если выражение 1 ложно то выражение 2 игнорируется возвращается результат выражения1
# Если выражение 1 истино то вернется результат выражения 2 вне зависимости True оно или False

my_list = [1, 2]
my_dict = {}
print(my_list and my_dict)

my_list = [1,3]
my_dict = {'a': 5}

my_list and print('В первом выражении есть данные')

# Логический оператор or(ИЛИ)

# Есть Выражение 1 и Выражение 2 Если выражение 1 истино то выражение 2 игнорируется возвращает результат выражение 1

my_list = []
other_list = ['a', 'b']
print(my_list or other_list)

my_list = [1, 2]
other_list = ['a', 'b']
print(my_list or other_list)

my_list = [1, 2]
other_list = ['a', 'b']
print(len(my_list) > 0 or other_list)

my_list = [1, 2]
other_list = ['a', 'b']
print(len(my_list) < 0 or other_list)
