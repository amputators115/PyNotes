# Целые числа

# Конвертация строки в число
# Запускать в терминале предварительно закоментив не нужный код

age = int(input('Введите ваш возраст: '))

print(age)
print(type(age))


# Конвертация с промежуточной переменной

age = input('Введите ваш возраст: ')
age_num = int(age)

print(age_num)
print(type(age_num))

# Запускать в code-runner

age = int('56')
print(age)
print(type(age))

# Привдение к целому с плавающей точкой
# Запускать в code-runner

my_num = int(5.789)
print(my_num)
print(type(my_num))

# Приведение к целому числу булевого значения
# Запускать в code-runner

bol = int(True)
print(bol)
print(type(bol))

bol = int(False)
print(bol)
print(type(bol))

# Возведение в степень с помощью pow()
# Запускать в code-runner

base = 2
power = 2
print(pow(base, power))
print(type(pow(base, power)))

# Возведение в стпень с помощью **
# Запускать в code-runner

print(3**2)

#Длинные числа можно разделять занком _ для удобства чтения, интерпритатор игнорирует
# Запускать в code-runner

one_mill = 1_000_000
print(one_mill)

one_hund = 1_000
print(one_hund)







