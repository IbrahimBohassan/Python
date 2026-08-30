import sys

nums = [float(x) for x in sys.argv[1:]]
print("Sum:", sum(nums))

# The command line for m and c
# >>python3 -c "import sys; print(sum(map(int, sys.argv[1:])))" 10 20 30
# >>python3 -m my_tools.calculator 10 20 30