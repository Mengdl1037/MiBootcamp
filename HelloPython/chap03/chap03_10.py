# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

destinations = ['Xizang', 'Sichuan', 'Yunnan', 'Shanghai', 'Hainan']

print('目的地：')
print(destinations)
print('正序排列：')
print(sorted(destinations))
print('反序排列：')
print(sorted(destinations, reverse = True))
print('原目的地列表不变：')
print(destinations)

print('翻转原列表：')
destinations.reverse()
print(destinations)

print('再次翻转原列表：')
destinations.reverse()
print(destinations)

print('原列表正序排列：')
destinations.sort()
print(destinations)
print('原列表反序排列：')
destinations.sort(reverse = True)
print(destinations)
