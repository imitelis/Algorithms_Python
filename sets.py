# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}


# add()
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# remove()
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Note: If you try to remove an element that is not in the set, it will raise a KeyError. 
# To avoid this, you can use the discard() method, which removes the element if it exists, or does nothing if the element is not found.

# discard()
my_set.discard(10)  # Does nothing because 10 is not in the set


# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# intersection()
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# difference()
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}


# Set iteration
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
# Output: 1, 2, 3, 4, 5 (order may vary as sets are unordered)

# Set comprehension
squared_numbers = {x**2 for x in range(1, 6)}
print(squared_numbers)  # Output: {1, 4, 9, 16, 25}
