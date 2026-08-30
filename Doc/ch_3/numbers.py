# =======================
# Basic Arithmetic Operations
# =======================

# >>> 2 + 2 
print("2 + 2 = ", 2 + 2)

# >>> 50 - 5 
print("50 - 5 = ", 50 - 5)

# >>> 50 - 5 * 6
print("50 - 5 * 6 = ", 50 - 5 * 6)

# >>> (50 - 5 * 6) / 4
print("(50 - 5 * 6) / 4 = ", (50 - 5 * 6) / 4)

# >>> 8 / 5
# division always returns a floating-point number
print("8 / 5 (float division) = ", 8 / 5)

# >>> 17 / 4 
# classic division return a float 
print("17 / 4 (classic division) = ", 17 / 4)

# >>> 17 / 3 
# classic division return a float
print("17 / 3 (classic division) = ", 17 / 3)

# =======================
# Floor Division and Modulo
# =======================

# >>> 17 // 3 
# floor division discard the fractional part
print("17 // 3 (floor division) = ", 17 // 3)

# >>> 17 % 3 
# the % operator returns the remainder of the division 
print("17 % 3 (remainder) = ", 17 % 3)

# >>> 5 * 3 + 2 
# floored qoutient * divisor + remainder
print("5 * 3 + 2 = ", 5 * 3 + 2)

# =======================
# Exponentiation (Powers)
# =======================
# Down we use ** operator to calculate powers:

# >>> 5 ** 2 
# 5 squared 
print("5 ** 2 (5 squared) = ", 5 ** 2)

# >>> 2 ** 7 
# 2 to the power of 7 
print("2 ** 7 (2 to the power of 7) = ", 2 ** 7)

# =======================
# Variables and Assignments
# =======================
# Down we use equal sign to assign a value to variable:

width = 30
height = 20
print("The width = ", width)
print("The height = ", height)
print("The result of width * height = ", width * height)

# =======================
# Calculations & Reusing Last Expression (_)
# =======================
# Note: In interactive Python shell (REPL), `_` holds the last printed result.
# In a standard script, we explicitly update the variable to demonstrate the exact same behavior.

tax = 12.50 / 100
price = 100.50

result = price * tax
print("The result of tax = ", result)

_ = result  # Replicating REPL behavior where _ holds the last value

total_price = price + _
print("The result of price + _ = ", total_price)

_ = total_price  # Updating _ to the latest result

rounded_total = round(_, 2)
print("The result of round(_, 2) = ", rounded_total)