my_dict = {'name': 'Hayaam', 'age': '10'}

print(my_dict['name'])
print(my_dict['age'])

my_dict['age'] = 11
print(my_dict)

my_dict['address'] = 'Peshawar, University Town, Proffesors Colony'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address :", my_dict.get('address'))

my_dict.clear()
print(my_dict)

