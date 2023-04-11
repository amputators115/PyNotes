# Встроенная функция Zip 
# Объедиянет типы данных причем они могут быть разными

computer = ['ibm', 'apple', 'dell']
price = (1000, 2000, 3000)
my_table = zip(computer, price)
print(my_table)
my_table = list(my_table)
print(my_table)

computer = ['ibm', 'apple', 'dell']
price = [1000, 2000, 3000]
my_table = zip(computer, price)
print(my_table)

# Конвертация в список кортежей

my_table = list(my_table)
print(my_table)

# Конвертация в словарь

computer = ['ibm', 'apple', 'dell']
price = [1000, 2000, 3000]
my_table = zip(computer, price)
my_table = dict(my_table)
print(my_table)



