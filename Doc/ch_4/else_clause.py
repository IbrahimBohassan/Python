
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "Equals", x, "*", n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("=========================")
print("     Another Example     ")
print("=========================")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can not divide by zero!")
else:
    print("Success! Result is = ", result)