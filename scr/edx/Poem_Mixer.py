def word_mixer(word_list):
    word_list.sort()
    new_list = []
    while len(word_list) > 5:
        new_list.append(word_list.pop(-5))
        new_list.append(word_list.pop(0))
        new_list.append(word_list.pop(-1))
    return new_list


poem_input = input("Enter poem: ")
split_poem = poem_input.split()
list_length = len(split_poem)
for x in range(len(split_poem)):
    if len(split_poem[x]) <= 3:
        split_poem[x] = split_poem[x].lower()
    elif len(split_poem[x]) >= 7:
        split_poem[x] = split_poem[x].upper()
print(" ".join(word_mixer(split_poem)))
