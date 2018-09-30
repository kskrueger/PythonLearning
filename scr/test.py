def printFib(input):
    output = ''
    fib_list = [0, 1]
    for x in range(0, input - 2):
        length = len(fib_list)
        sum = fib_list[length - 2] + fib_list[length - 1]
        fib_list.append(sum)
    for x in fib_list:
        output += str(x) + ","
    print(str(output))


printFib(6)


def matrix_funct():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for y in range(0, len(matrix)):
        output = ''
        for x in range(0, len(matrix[y])):
            output += str(matrix[y][x]) + " "
        print(output)
