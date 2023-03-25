# Магические методы

rost = 176
temp = 37.6

print(rost.__add__(temp))
print(temp.__radd__(rost))
print(temp.__add__(rost))

age = bool(25)
print(age)
print(dir(age))  # вызов списка методов
print(dir(bool))  # вызов списка методов
print(dir(None))  # вызов списка методов

# вызов вызов документации для класса

print(bool.__doc__)
print(int.__doc__)
print(list.__doc__)
print(dict.__doc__)
print(float.__doc__)
print(tuple.__doc__)
print(dir.__doc__)
print(round.__doc__)  # и так далее

# Информация о кокретном магическом методе

print(help(str.__eq__)) 
print(help(str.__add__))
