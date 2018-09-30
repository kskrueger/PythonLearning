user_name = input("Enter your name: \n")
print("Hi " + user_name)
seed = len(user_name)
pi_file = open('scr/pi.txt', 'r')
guess = 0
correct = 0
wrong = 0
while guess is not "q":
    pi_file.seek(seed)
    digit = pi_file.read(1)
    guess = input("""Enter a single digit guess or "q" to quit: \n""")
    if digit is ".":
        seed += 1
        pi_file.seek(seed)
    elif digit is "\n":
        seed += 1
        pi_file.seek(seed)
    elif guess is digit:
        correct += 1
        print("Correct")
    else:
        wrong += 1
        print("Wrong")

print("Correct: " + str(correct))
print("Wrong: " + str(wrong))
pi_file.close()
