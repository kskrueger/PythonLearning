import random
low = 1
high = 5

a = int(input("Guess a number between "+str(low)+" and "+str(high)))
print("You chose "+str(a))
b = random.randint(low,high)
if a == b:
    print("You guessed it right!")
else:
    print("You guessed incorrect")
    print("The correct value was "+str(b))