# Задача по наборам

# 1 Создайте набор с нескольких элементов типа int
# 2 Добавьте в него еще один элемент
# 3 Создайте еще один набор причем в нем длны находиться несколько схожих элементов с 1 го набора
# 4 Найдите общие элементы в двух наборах и поместите их в новый набор
# 5 Конвертируйте результирующий набор в список и выведите их в терминал

set_one = {12, 54, 67}  # 1
set_one.add(56)  # 2
set_two = {12, 54, 67, 71}  # 3
new_set = set_one.intersection(set_two)  # 4
print(list(new_set))  # 5
