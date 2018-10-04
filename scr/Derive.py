equation_input = input("Input an equation in terms of x (ex: 5x^2+2x) ")
addition_terms = equation_input.split("+")
output = ""
for term in addition_terms:
    exponent_split = term.split("^")
    new_out = str(str(exponent_split[1]) + "*" + exponent_split[0] + "^" + str(int(exponent_split[1]) - 1))
    new_out = new_out.replace("x^0", "")
    new_out = new_out.replace("x^1", "x")
    if "x" not in new_out:
        new_out = eval(str(new_out))
    output += str(new_out)+"+"
print(output[:-1])