# Методы списков объекты наследуют от класса list

# append() - добавляет новые в конец списка
# мутирует объект можно убедиться через передачу id

my_num = []
my_num.append(78)
my_num.append('Ivan')
print(my_num)
print(len(my_num))
print(type(my_num))


# мутирует объект можно убедиться через передачу id

my_num = []
print(my_num)
print(id(my_num))
my_num.append(78)
my_num.append('Ivan')

new_num = my_num

print(new_num)
print(id(new_num))

# pop() - удаление элементов из списка
# мутирует объект можно убедиться через передачу id
# без передачи аргумента удалит последний элемент

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(len(my_num))
my_num.pop()
print(my_num)
print(len(my_num))

# с передачей аргумента удалит элемент по индексу

my_num = [1, 56, 78, 678, 876.8]
print(my_num)
print(len(my_num))
my_num.pop(2)
print(my_num)
print(len(my_num))

# pop возвращает удаленный элемент

my_num = [1, 56, 78, 678, 876.8]
my_num.pop(2)
remove_elem = my_num.pop(2)
print(my_num)
print(remove_elem)

# sort() - сортировка элементов в списке
# без передачи аргумента отсортирует по возрастанию
# мутирует объект можно убедиться через передачу id

my_num = [1, 78, 54, 678, 876.8]
my_num.sort()
print(my_num)

# с передачей аргумента отсортирует по убыванию

my_num = [1, 78, 54, 678, 876.8]
my_num.sort(reverse=True)
print(my_num)

# remove() - удаление по значению
# можно использовать, когда мы точно знаем значение, от которого хотим избавиться. В качестве аргумента remove() получает объект, находит совпадение и удаляет его, ничего не возвращая

my_num = [1, 78, 54, 678, 876.8]
my_num.remove(1)
print(my_num)

# insert() - вставляет элемент в список по указанному индексу(индекс и что передаем)

my_num = [1, 78, 54, 678, 876.8]
my_num.insert(3, 'ivan')
print(my_num)

# index() - позволяет узнать индекс или позицию элемента в последовательности.

my_num = [1, 78, 54, 678, 876.8]
print(my_num.index(678))

# clear() удаляет все элементы из списка.

my_num = [1, 78, 54, 678, 876.8]
print(my_num)
print(my_num.clear())
print(my_num)

# copy() - копирование списка

my_num = [1, 78, 54, 678, 876.8]
print(my_num)
new_num = my_num.copy()
print(new_num)

# count() возвращает количество повторений, когда указанный элемент появляется в списке.

my_num = [1, 78, 54, 1, 678, 876.8, 1]
new_num = my_num.count(1)
print(new_num)
