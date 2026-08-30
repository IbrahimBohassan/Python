# =======================
# Fibonacci Series & Print Customization
# =======================
# Down we use Fibonacci series:
# the sum of two elements defines the next

print("Fibonacci loop output (< 10):")
a, b = 0, 1
while a < 10:
    print("Current value of a: ", a)
    a, b = b, a + b

i = 256 * 256
print('The value of i is = ', i)

print("Fibonacci series output with comma separator (< 1000):")
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a + b
print() # Print newline at the end