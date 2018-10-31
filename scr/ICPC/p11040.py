input0 = input()
input_all = input0.split("\n")
cases = int(input_all[0])  # int(input())
for case in range(0, cases):
    arrays = []
    for i in range(1, 10):
        array = [0] * i
        arrays.append(array)

    for i in range(0, 9, 2):
        input_arr = input_all[int(i/2)+1]  # input()
        input_arr = input_arr.split()
        for l in range(0, i + 1, 2):
            arrays[i][l] = input_arr[int(l / 2)]

    for i in range(2, 9, 2):
        for l in range(1, i, 2):
            arrays[i][l] = int((int(arrays[i-2][l-1]) - (int(arrays[i][l-1]) + int(arrays[i][l+1]))) / 2)

    for i in range(1, 8, 2):
        for l in range(0,i+1):
            arrays[i][l] = int(arrays[i+1][l]) + int(arrays[i+1][l+1])

    for i in range(0, 9):
        out = ""
        for l in range(0, i+1):
            out += (str(arrays[i][l]))
            if l < i:
                out += " "
        print(out)
