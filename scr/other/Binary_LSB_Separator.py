file = open("bin_dump", "r")
final_out = ""
line = file.readline()
while line:
    values = line[10:-9]
    num_list = values.split(" ")
    for num in num_list:
        final_out += num[-1:]
    line = file.readline()

bytes_total = ""
data = final_out[:32]
# print("Pre data: ", data)
# print("pre num: ", int(data, 2))
while data:
    bytes_total += data[-8:]
    data = data[:-8]

# print("Bytes to pull: ", bytes_total)
# print("Bytes to pull: ", int(bytes_total, 2))
# print(final_out[32:int(bytes_total, 2)*8])
print("Full len: ", len(final_out))
