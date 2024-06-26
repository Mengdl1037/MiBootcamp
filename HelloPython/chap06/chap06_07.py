# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

people1 = {}
people1['first_name'] = 'Zhang'
people1['last_name'] = 'San'
people1['age'] = 18
people1['city'] = 'Beijing'

people2 = {}
people2['first_name'] = 'Li'
people2['last_name'] = 'Si'
people2['age'] = 19
people2['city'] = 'Wuhan'

people3 = {}
people3['first_name'] = 'Wang'
people3['last_name'] = 'Wu'
people3['age'] = 19
people3['city'] = 'Shanghai '

people = [people1, people2, people3]

for person in people:
    for key, value in person.items():
        print(f'{key}: {value}')
    print('\n')