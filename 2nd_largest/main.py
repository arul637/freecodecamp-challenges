def first_largest(arr):
    max = 0

    for number in arr:
        if number > max:
            max = number 
    
    return max


def second_largest(arr):

    first_largest_number = first_largest(arr)

    second_largest_number = 0

    for number in arr:
        if number == first_largest_number:
            continue
        if number > second_largest_number:
            second_largest_number = number 

    return second_largest_number 


print(second_largest([1, 2, 3, 4]))
print(second_largest([20, 139, 94, 67, 31]))
print(second_largest([2, 3, 4, 6, 6]))
print(second_largest([10, -17, 55.5, 44, 91, 0]))
print(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]))
