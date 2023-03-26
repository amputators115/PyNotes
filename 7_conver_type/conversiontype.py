#Конвертация типов явная с помощью встроенных функций
# 1. В строку str()

print(str(5) + '10')

age_one = '10'
age_two = 5
summ = age_one + str(age_two)
print(summ)

age_one = '10'
age_two = str(5)
print(age_one + age_two)

# 2. В целое число int()

print(5 + int('10'))

age_one = '10'
age_two = 5
summ = int(age_one) + age_two
print(summ)

age_one = int('10')
age_two = 5
print(age_one + age_two)



# 3. В число с десятичной float()

# Ошибка

5 + '10'

print(0.7 + 5)

int_num = 7
fl_num = 4.78
print(fl_num + int_num)

# Не будет ошибкой не явная конвертация

print(5 + 10.7)
print(5 * 10.7)
print(5.6 * 10)
print(5.8 + 10)

int_num = 7
fl_num = 4.78
print(int_num * fl_num)

print(True + 7)
print(7 + True)
print(7 + False)
