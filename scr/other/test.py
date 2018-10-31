txt_file = open('text.txt', 'r')
all_text = txt_file.read()
array = [0] * 26
for letter in all_text:
    if 'z' > letter > 'a':
        array[ord(letter) - ord('a')] += 1

for x in range(len(array)):
    print(chr(x+ord('a')), ":", array[x])
