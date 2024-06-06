# п. 1 Функция должна выводить эти параметры.

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()

print_params(3, 4, 5)

print_params(b=25)

print_params(c=[1, 2, 3])

# п2. Распаковка параметров:

values_list = [1, 'rrrrrr', True]
values_dict = {'a': 2, 'b': 'ggggg', 'c': False}

print_params(*values_list)

print_params(**values_dict)

# 3. .Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка' ]

print_params(*values_list_2, 42)