# 1. Variable Creations
my_int = 5
my_str = "hello"
my_list = [10, 20, 30]
my_dict = {"a": 1, "b": 2, "c": 3}

# --- 2. Using '+' operator ---
print("=== '+' Operator ===")
print("int: ", my_int + 10)
print("str: ", my_str + " world")
print("list:", my_list + [40, 50])

# --- 3. Using '*' operator ---
print("\n=== '*' Operator ===")
print("int: ", my_int * 3)
print("str: ", my_str * 3)
print("list:", my_list * 2)

# --- 4. Using len() function ---
print("\n=== len() Function ===")
print("str: ", len(my_str))
print("list:", len(my_list))
print("dict:", len(my_dict))

# --- 5. Using 'in' operator ---
print("\n=== 'in' Operator ===")
print("str: ", "e" in my_str)
print("list:", 20 in my_list)
print("dict:", "b" in my_dict)  

# --- 6. Using 'for' loop ---
print("\n=== 'for' Loop ===")

print("str iteration:")
for char in my_str:
    print("  ", char)

print("list iteration:")
for item in my_list:
    print("  ", item)

print("dict iteration:")
for key in my_dict:
    print(f"   key: {key}, value: {my_dict[key]}")