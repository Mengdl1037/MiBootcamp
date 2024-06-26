# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

pet1 = {}
pet1['name'] = 'dog'
pet1['owner'] = 'Zhang San'

pet2 = {}
pet2['name'] = 'cat'
pet2['owner'] = 'Li Si'

pet3 = {}
pet3['name'] = 'dog'
pet3['owner'] = 'Wang Wu'


pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f'{key}: {value}')
    print('\n')