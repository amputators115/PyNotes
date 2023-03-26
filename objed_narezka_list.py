# Объединение списков

my_num = [1, 56, 78, 678, 876.8]
two_dict = ['Msc', 'ivan', 56, 78.9]
print(my_num + two_dict)

# Нарезка списков

my_num = [1, 56, 78, 678, 876.8]
print(my_num[:2])
print(my_num[1:5])
print(my_num[:2])
print(my_num[-1])
print(my_num[1:-1])
print(my_num[-2])

# Копирование списков
# При таком способе прлучаем полные копии
my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(id(my_num))
new_num = my_num
print(id(new_num))

# При добавлении элемента в новый список происходит мутация исходника

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(id(my_num))
print(len(my_num))

new_num = my_num
new_num.append('vova')
print(my_num)
print(new_num)
print(id(new_num))
print(len(new_num))
print(new_num == my_num)
print(id(new_num) == id(my_num))

# Копирование без мутации

# 1 Метод [:] - копирование через нарезку

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(id(my_num))
print(len(my_num))

new_num = my_num[:] #копируем объект
new_num.append('vova')
print(my_num)
print(new_num)
print(id(new_num))
print(len(new_num))
print(new_num == my_num)
print(id(new_num) == id(my_num))

# 2 Копирование через метод copy() 

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(id(my_num))
print(len(my_num))

new_num = my_num.copy()  # копируем объект
new_num.append('vova')
print(my_num)
print(new_num)
print(id(new_num))
print(len(new_num))
print(new_num == my_num)
print(id(new_num) == id(my_num))

# 2 Копирование через встроенную функцию list()

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(id(my_num))
print(len(my_num))

new_num = list(my_num)  # копируем объект
new_num.append('vova')
print(my_num)
print(new_num)
print(id(new_num))
print(len(new_num))
print(new_num == my_num)
print(id(new_num) == id(my_num))

