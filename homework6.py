my_dict = {'Bogdan': 1997, 'Anton': 1995, 'Georgy': 1996}
print(my_dict)
print(my_dict['Bogdan'])
print(my_dict.get('Sasha'))
my_dict.update({'Alex': 1993, 'Petr': 1990})
my_dict.pop('Alex')
print(my_dict)


my_set = {1, 1, True, True, False, False, 'Petr', 'Petr'}
print(my_set)
my_set.add(7)
my_set.add(9)
my_set.remove(True)
print(my_set)