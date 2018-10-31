# python
user_input = input("Input in format A op B")
input_sep = user_input.split()
input_a = int(input_sep[0])
operator = input_sep[1]
input_b = int(input_sep[2])

if operator is '+':
    print(int(input_a + input_b))
elif operator is '-':
    print(int(input_a - input_b))
