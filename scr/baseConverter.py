def from_base_10():
    number = int(input("Input a number: "))
    base = int(input("Input output base: "))

    max_power = 0
    while number / base ** max_power > 1:
        max_power += 1

    output = 0
    last_num = number
    for x in range(max_power, -1, -1):
        power = (base ** x)
        output += int(last_num / power) * 10 ** x
        last_num %= power

    print("Output: " + str(output))


from_base_10()
