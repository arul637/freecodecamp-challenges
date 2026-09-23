from typing import List 

def find_target(arr: List, target) -> List:

    output_array = []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (i != j) and (arr[i] + arr[j]) == target:
                output_array = [i, j]

    if output_array == []:
        return 'Target not found'

    return output_array

print(find_target([2, 7, 11, 15], 9))
print(find_target([3, 2, 4, 5], 6))
print(find_target([1, 3, 5, 6, 7, 8], 15))
print(find_target([1, 3, 5, 7], 14))