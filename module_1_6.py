my_dict={'Peter': 1981, 'Max': 1976, 'Den': 1972, 'Vlad': 1977, 'Alex': 1980}
print (my_dict)
print (my_dict['Vlad'])
print (my_dict.get('Bob'))
my_dict.update({'Mike': 1972, 'Anna': 1983})
print(my_dict)
c = my_dict.pop('Den')
print(c)
print(my_dict)

