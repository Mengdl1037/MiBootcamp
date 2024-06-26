# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def create_car_info(manufacturer, model, **car_info):
    """Create a dictionary of car information
    Args:
        manufacturer: the manufacturer of the car
        model: the model of the car
        **car_info: other information of the car
    Returns:
        a dictionary of car information
    """
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = create_car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)