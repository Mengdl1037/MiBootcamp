# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

rivers = {}

rivers['nile'] = 'egypt'
rivers['changjiang'] = 'china'
rivers['huanghe'] = 'china'

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
print('\n')

for river in rivers.keys():
    print(river.title())
print('\n')

for country in rivers.values():
    print(country.title())
print('\n')
