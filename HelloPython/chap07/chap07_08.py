# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

phone_orders = ['14Type1', '14Type2', '14Type1', '14Type3', '14Type4']
finished_orders = []

while phone_orders:
    finished_orders.append(phone_orders.pop(0))

print("The following orders have been finished:")
for finished_order in finished_orders:
    print(finished_order, end=' ')