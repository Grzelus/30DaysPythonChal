def multiply(number: int):
    result = []
    result.append(number)
    for i in range(4):
        result.append(number**i)

    return result

for i in range(1, 6):
    row = multiply(i)
    for j in range(len(row)):
        print(row[j], end=" ")
    print('')
