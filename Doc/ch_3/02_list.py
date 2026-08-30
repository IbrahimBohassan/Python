# =======================
# Lists Operations
# =======================
# Down we use list:

square = [1, 4, 9, 16, 25]
print("List square: ", square)
print("Index square[0]: ", square[0])
print("Index square[-1]: ", square[-1])
print("Slice square[-3:]: ", square[-3:])
print("Concatenated list: ", square + [36, 49, 64, 81, 100])

# Down we use mutable list:
cubes = [1, 8, 27, 65, 125] # something's wrong here
print("Calculated 4 ** 3: ", 4 ** 3)
cubes[3] = 64 # replace the wrong value
print("Corrected cubes list: ", cubes)

# Down we use list.append():
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # add the cube of 7
print("List after append operations: ", cubes)

# =======================
# Object References & Shallow Copy
# =======================
# Down we use the reference of the same Object:

rgb = ["Red", "Green", "Blue"]
rgba = rgb
print("Are rgb and rgba referencing the same object? ", id(rgb) == id(rgba))

rgba.append("Alph")
print("Updated rgb: ", rgb)
print("Updated rgba: ", rgba)

# Down we use shallow copy:
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print("Shallow copied correct_rgba: ", correct_rgba)
print("Original rgba remains: ", rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original letters list: ", letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print("After replacing slice letters[2:5]: ", letters)

# now remove them
letters[2:5] = []
print("After removing slice letters[2:5]: ", letters)

# clear the list by replacing all elements with an empty list
letters[:] = []
print("After clearing list letters[:]: ", letters)

# =======================
# Nested Lists
# =======================
# Down we use list inside another list

letters = ['a', 'b', 'c', 'd']
print("Length of letters: ", len(letters))

a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print("Nested list x: ", x)
print("Index x[0]: ", x[0])
print("Index x[0][1]: ", x[0][1])
print("Index x[1][0]: ", x[1][0])