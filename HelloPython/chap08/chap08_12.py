# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def create_sandwich_order(*ingredients):
    """Print the ingredients of a sandwich
    Args:
        ingredients: a list of ingredients
    Returns:
        None
    """
    print('The sandwich includes:')
    for ingredient in ingredients:
        print(ingredient)


create_sandwich_order('tomato', 'potato', 'cucumber', 'egg')
create_sandwich_order('cucumber', 'egg')
create_sandwich_order('tomato', 'potato', 'cucumber')