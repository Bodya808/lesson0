def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(c=[1, 2, 3], a=42)

values_list = ["строка", 25, [1, 2, 3]]
values_dict = {'a': 42, 'b': 'другая строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
