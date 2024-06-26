# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

cities = {}
cities['Beijing'] = \
    {'country': 'China', 'population': 21_893_100, 'fact': 'capital'}
cities['Wuhan'] = \
    {'country': 'China', 'population': 13_648_900, 'fact': 'river city'}
cities['Shanghai'] = \
    {'country': 'China', 'population': 26_875_500, 'fact': 'economic center'}

for city, info in cities.items():
    print(f'{city}:')
    for key, value in info.items():
        print(f'\t{key}: {value}')
    print('\n')