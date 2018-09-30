temp_file = open('scr/mean_temp.txt', 'r')
headings = temp_file.readline()
print(headings)
headings_list = headings.split(',')
print(headings_list)

line = temp_file.readline()
while line:
    city_list = line.split(',')
    print(city_list[0] + ": " + city_list[2])
    line = temp_file.readline()
