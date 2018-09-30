def get_names():
    print("list any 5 of the first 20 elements in the Period table\n")
    correct_list = []
    wrong_list = []
    element_file = open('elements3.txt', 'r')
    # element_list = element_file.read().split('\n')
    element_list = []
    line = element_file.readline()
    while line:
        element_list.append(line.strip("\n"))
        line = element_file.readline()
    for x in range(0, len(element_list)):
        element_list[x] = element_list[x].lower()
    correct_count = 0
    wrong_count = 0
    user_input = ' '
    while user_input is not '' and (correct_count + wrong_count) < 5:
        user_input = str(input("Enter the name of an element: \n")).lower()
        if element_list.count(user_input) > 0:
            if correct_list.count(user_input) > 0:
                print(user_input + " was already entered\n")
            else:
                correct_list.append(user_input)
                correct_count += 1
        else:
            print("Not in list")
            wrong_list.append(user_input)
            wrong_count += 1
    print("Correct " + str(correct_count / (correct_count + wrong_count) * 100) + " %")
    correct = ''
    for element in correct_list:
        correct += element[0].upper() + element[1:] + " "
    wrong = ''
    for element in wrong_list:
        wrong += element[0].upper() + element[1:]
    print("Found: " + correct)
    print("Not Found: " + wrong)
    return correct_list
