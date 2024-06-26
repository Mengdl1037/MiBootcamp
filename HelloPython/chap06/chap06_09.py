# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

favorite_places = {}

favorite_places['Zhang San'] = ['Beijing', 'Shanghai', 'Wuhan']
favorite_places['Li Si'] = ['Beijing', 'Shanghai']
favorite_places['Wang Wu'] = ['Beijing', 'Shanghai', 'Wuhan', 'Guangzhou']

for name, places in favorite_places.items():
    print(f'{name} likes the following places:')
    for place in places:
        print(f'\t{place}')
    print('\n')