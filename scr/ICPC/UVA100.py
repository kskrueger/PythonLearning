n = int(input())
out = ""
while 1:
    out += str(n)+" "
    if n is 1:
        break
    if n % 2 is 1:
        n = int(n * 3 + 1)
    else:
        n = int(n/2)
print(out)
