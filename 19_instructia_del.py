# Инструкция del

my_dict = {'a': 10, 'b': 30}
del my_dict['a']
my_dict.__delitem__('b')  # Магический метод
print(my_dict)

my_list = [1, 3, 4, 5]
del my_list[0]
my_list.__delitem__(1)  # Магический метод
print(my_list)





