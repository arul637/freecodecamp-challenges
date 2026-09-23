def tribonacci_sequence(start_sequence, length):

    if length <= len(start_sequence):
        return start_sequence[:length]

    for i in range(length-3):
        start_sequence += [sum(start_sequence[i:i+3])]

    return start_sequence

print(tribonacci_sequence([0, 0, 1], 20))
print(tribonacci_sequence([21, 32, 43], 1))
print(tribonacci_sequence([0, 0, 1], 0))
print(tribonacci_sequence([10, 20, 30], 2))
print(tribonacci_sequence([10, 20, 30], 3))
print(tribonacci_sequence([123, 456, 789], 8))