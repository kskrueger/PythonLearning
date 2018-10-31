# python
user_input = str(input("n a"))
input_sep = user_input.split()
n = int(input_sep[0])
a = int(input_sep[1])
sum_out = 0
for num in range(0, n+1):
    sum_out += num * pow(a, num)

print(str(sum_out))

