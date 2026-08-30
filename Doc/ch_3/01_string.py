# =======================
# Basic Strings Examples
# =======================

# >>> ' qoute ' # single qoutes
print("Single quotes example: ", ' qoute ')

# >>> " A warm smile is the universal language of kindness :)! William Arthur Ward" # double qoutes
print("Double quotes example: ", " A warm smile is the universal language of kindness :)! William Arthur Ward")

# >>> ' 1968 ' # digits and numeral enclosed in qoutes are also strings
print("Digits as string: ", ' 1968 ')

# =======================
# Escaping Characters (\)
# =======================
# Down we use escape \:

# >>> ' doesn\'t' # use \' to escape the single qoute...
print("Escaped single quote: ", ' doesn\'t')

# >>> "doesn't" # ...or use double qoutes instead
print("Double quotes avoiding escape: ", "doesn't")

# >>> '"Yes," they said.'
print("Mixed quotes 1: ", '"Yes," they said.')

# >>> "\"Yes,\" they said."
print("Mixed quotes 2 (escaped): ", "\"Yes,\" they said.")

# >>> '"Isn\'t," they said.'
print("Mixed quotes 3 (escaped): ", '"Isn\'t," they said.')

# =======================
# Using print() vs Raw Output
# =======================
# Down we use print() function:

s = 'First line.\nSecond line.' # \n means newline
# >>> s # without print(), special characters are included in the string
print("String representation without print evaluation: ", repr(s))

# >>> print(s) # with print(), special characters are interpreted, so \n produces new line
print("Evaluated string with print():")
print(s)

# =======================
# Raw Strings
# =======================
# Down we use the raw string by adding ad r before the first qoute:

# >>> print('C:\this\name') # here \t means tab, \n means newline
print("Normal string with escape characters:")
print('C:\this\name')

# >>> print(r'C:\this\name') # note the r before the qoute
print("Raw string output:")
print(r'C:\this\name')

# =======================
# Multi-line Triple Quotes
# =======================
# Down we use triple-qoutes to sapn multiple lines:

print("Triple-quoted multi-line output:")
print("""\
Usage: thingy [OPTIONS]
     -h                         Display this usage message
     -H hostname                Hostname to connect to
""")

# =======================
# String Concatenation & Repetition
# =======================
# Down we use + to glue together and repeated with *:

# >>> 3 * 'un' + 'ium'
print("Repetition and concatenation (3 * 'un' + 'ium'): ", 3 * 'un' + 'ium')

# Down we use two or more strings literals next to each other are autmoatically concatenated
print("Implicit literal concatenation: ", 'Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print("Parentheses concatenated string: ", text)

# Down is a syntax error:
# Note: Handled using try-except to allow the script to execute completely without crashing.
print("Syntax error demonstration: Cannot concatenate a variable and a string literal without standard + operator.")
try:
    prefix = 'Py'
    exec("prefix 'thon'")
except SyntaxError as e:
    print("Caught SyntaxError: ", e)

try:
    exec("('un' * 3) 'ium'")
except SyntaxError as e:
    print("Caught SyntaxError: ", e)

# Down we concatenate variable:
postfix = 'thon'
print("Concatenation with + operator (prefix + postfix): ", prefix + postfix)

# =======================
# String Indexing & Slicing
# =======================
# Down we can use string as indexed positive from left to right and negative from right to left:

word = 'Python'
print("Index 0 of word: ", word[0])
print("Index 5 of word: ", word[5])
print("Index -1 of word: ", word[-1])
print("Index -2 of word: ", word[-2])
print("Index -6 of word: ", word[-6])

print("Slice word[0:2]: ", word[0:2])
print("Slice word[2:5]: ", word[2:5])
print("Slice word[:2]: ", word[:2])
print("Slice word[4:]: ", word[4:])
print("Slice word[-2:]: ", word[-2:])
print("Slice word[:2] + word[2:]: ", word[:2] + word[2:])
print("Slice word[:4] + word[4:]: ", word[:4] + word[4:])

# Down is a syntax error (IndexError):
try:
    print(word[42])
except IndexError as e:
    print("Caught IndexError (word[42]): ", e)

# =======================
# Immutability & Modifications
# =======================
# Down we use string immutable:

try:
    word[0] = 'j'
except TypeError as e:
    print("Caught TypeError (string immutability item assignment): ", e)

try:
    word[2:] = 'py'
except TypeError as e:
    print("Caught TypeError (string immutability slice assignment): ", e)

# Down we can make diff in string:
print("Created new string with 'J' + word[1:]: ", 'J' + word[1:])
print("Created new string with word[:2] + 'py': ", word[:2] + 'py')

# Down we use len():
s = 'supercalifragilisticexpialidocious'
print("Length of string 'supercalifragilisticexpialidocious': ", len(s))