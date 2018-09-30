def list_o_matic():
    numbers = ["one", "two", "three", "four", "five"]
    while True:
        word = str(input("Enter an item or type quit "))
        if word == "":
            numbers.pop()
            print("Removed last word")
        elif word in numbers:
            numbers.remove(word)
            print(word, "removed from list")
        elif word not in numbers:
            numbers.append(word)
            print(word, "added to list")
        if word == "quit":
            print("Quit")
            break
        if len(numbers) == 0:
            print("Empty: Quit")
            break


list_o_matic()
