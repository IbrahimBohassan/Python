for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            # print(f"{n} equal {x} * {n//x}")
            print(n, "equals", x, "*", n//x)
            break

print("=========================")
print("     Another Example     ")
print("=========================")

for num in range(2, 14):
    if num % 2 == 0:
        print("Found an even number = ", num)
        continue
    print("Found an odd number = ", num)

