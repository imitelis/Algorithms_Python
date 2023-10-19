single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"

multi_line = '''This is a multi-line
string in Python.'''

# String index
text = "Python"
print(text[0])   # Output: "P" (indexing starts from 0)
print(text[-1])  # Output: "n" (negative indexing from the end)

# Sring slice
text = "Python Programming"
substring = text[7:18]
print(substring)  # Output: "Programming" (includes character at index 7 but excludes character at index 18)


# len()
text = "Python"
print(len(text))  # Output: 6

# lower(), upper()
text = "Hello, World!"
print(text.lower())  # Output: "hello, world!"
print(text.upper())  # Output: "HELLO, WORLD!"

# strip(), lstrip(), rstrip()
text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"

# replace(old, new)
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)  # Output: "Hello, Python!"

# split(separator)
text = "apple,orange,banana"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'orange', 'banana']

# join(iterable)
fruits = ['apple', 'orange', 'banana']
text = ",".join(fruits)
print(text)  # Output: "apple,orange,banana"

# find(substring), index(substring)
text = "Hello, World!"
print(text.find("World"))  # Output: 7
print(text.index("World"))  # Output: 7
