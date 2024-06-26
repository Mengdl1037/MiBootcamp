# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:
import time

num_list = [value for value in range(1, 1_000_001)]
print("The minimum number in the list is: " + str(min(num_list)))
print("The maximum number in the list is: " + str(max(num_list)))

print("time consuming:")
start = time.time()
print(sum(num_list))
end = time.time()
print("Time consumed: %s seconds."  %str(end - start))