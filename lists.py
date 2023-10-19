# Creating an empty list
empty_list = []

# Creating a list with elements
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'banana']

# Lists can contain different data types
mixed_list = [1, 'hello', 3.14, True]

# Accessing elements by index (indexing starts from 0)
print(numbers[0])  # Output: 1
print(fruits[1])   # Output: 'orange'

# Slicing allows you to access a subset of the list
print(numbers[1:4])  # Output: [2, 3, 4]
print(fruits[:2])    # Output: ['apple', 'orange']


# append()
fruits.append('grape')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'grape']

# extend()
fruits.extend(['kiwi', 'melon'])
print(fruits)  # Output: ['apple', 'orange', 'banana', 'grape', 'kiwi', 'melon']

# insert()
fruits.insert(1, 'pear')
print(fruits)  # Output: ['apple', 'pear', 'orange', 'banana', 'grape', 'kiwi', 'melon']

# remove()
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'pear', 'banana', 'grape', 'kiwi', 'melon']

# pop()
removed_item = fruits.pop(2)
print(removed_item)  # Output: 'banana'
print(fruits)        # Output: ['apple', 'pear', 'grape', 'kiwi', 'melon']


# index()
print(fruits.index('grape'))  # Output: 2

# count()
print(fruits.count('pear'))  # Output: 1

# sort()
numbers = [5, 2, 9, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 9]

# reverse()
numbers.reverse()
print(numbers)  # Output: [9, 5, 5, 2, 1]
