def fizzbuzz(n):
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("fizzbuzz")
        elif i % 3 == 0:
            arr.append("fizz")
        elif i % 5 == 0:
            arr.append("buzz")
        else:
            arr.append(str(i))
    return arr

print(fizzbuzz(15))