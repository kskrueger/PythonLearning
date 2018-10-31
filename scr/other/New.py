print("Start")
for a in range(1, 10000):
    for b in range(1, 10000):
        for c in range(1, 10000):
            if (a*1.0 / (b + c) + b*1.0 / (a + c) + c*1.0 / (a + b)) == 10:
                print("A", a, "B", b, "C", c)
                break

print("End")
