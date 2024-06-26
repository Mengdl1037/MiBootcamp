# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

orientations = []

while True:
    orientation = \
        input("If you could visit one place in the world, where would you go?")
    orientations.append(orientation)
    active = input("Would you like to let another person respond? (yes/ no)")
    if active == 'no':
        break

print("\n--- Poll Results ---")
for orientation in orientations:
    print(orientation.title())