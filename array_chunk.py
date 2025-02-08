def chunk(arr, size):
    result = []
    index = 0
    while index < len(arr):
        result.append(arr[index : index + size])
        index += size
    return result

print(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5))