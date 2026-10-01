def array_diff(arr1, arr2):
    array1_copy = arr1 
    array2_copy = arr2 

    array = []
    array.extend(array1_copy)
    array.extend(array2_copy)

    array = list(set(array))

    for element in array:
        if element in array1_copy and element in array2_copy:
            array1_copy.remove(element)
            array2_copy.remove(element)

    array = []
    array.extend(array1_copy)
    array.extend(array2_copy)

    array = list(set(array))

    return array

print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))
print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
print(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]))
print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))
