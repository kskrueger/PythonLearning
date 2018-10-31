inputs = int(input())
output = []
for x in range(inputs):
    line_input = input()
    split_input = line_input.split(" ")
    if split_input[0] == split_input[1]:
        output += "="
    elif split_input[0] < split_input[1]:
        output += "<"
    elif split_input[0] > split_input[1]:
        output += ">"

for out in output:
    print(out)
