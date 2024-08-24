my_dict = {'Evgeny': 1985, 'Misha': 1976, 'Marina': 1988}
print('Dict:', (my_dict))
print('Existing value:', my_dict.get('Marina'))
print('Not existing value:', my_dict.get('Masha'))
my_dict.update({'Masha': 2000, 'Nastya': 2015})
print('Deleted value:', my_dict.pop('Masha'))
print('Modified dictionary:', my_dict)
#
my_set = {1, 'Lada', 36.6, 1, 'Lada', 36.6}
print('Set:', my_set)
my_set.update({2024, 'Niva'})
my_set.discard(36.6)
print('Modified set:', my_set)
