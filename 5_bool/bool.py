# Логические типы

work = True
print(work)
print(type(work))

work = False
print(work)
print(type(work))

print(100 > 6)
print(100 < 6)
print('long string' > 'string')
print('long string' < 'string')
print('Long string' > 'Short')
print('Long string' > 'Long')
print('Long string' > 'long')
print('long string' == 'string')
print('long string' != 'string')
print([1, 3, 4, 5] == [1, 3, 4, 5])
print([1, 3, 4, 5] != [1, 3, 4, 5])
print({'a': 45} == {'a': 47})

# Приведение к логическому типу данных bool

print(bool(3))
print(bool(0))
print(bool(23.6))
print(bool('age'))
print(bool(' '))
print(bool(''))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(None))


age = bool(27)
print(age)
print(type(age))

age = 27
new_age = bool(age)
print(new_age)
print(type(new_age))

age = 27
new_age = bool(age)
print(new_age)
print(type(new_age))
