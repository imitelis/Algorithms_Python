# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with elements
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing elements by keys
print(person["name"])  # Output: "Alice"
print(person["age"])   # Output: 30


# Modifying a Value
person["age"] = 31
print(person["age"])  # Output: 31

# Adding a New Key-Value Pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}


# keys(), values(), and items()
print(person.keys())    # Output: dict_keys(['name', 'age', 'city', 'job'])
print(person.values())  # Output: dict_values(['Alice', 31, 'New York', 'Engineer'])
print(person.items())   # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('job', 'Engineer')])

# get(key, default_value)
print(person.get("age"))          # Output: 31
print(person.get("salary", 0))    # Output: 0 (default value since "salary" key is not in the dictionary)

# pop(key, default_value)
person.pop("job")  # Removes the "job" key-value pair
print(person)      # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# update(dictionary)
additional_info = {"hobby": "Reading", "city": "Boston"}
person.update(additional_info)
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'Boston', 'hobby': 'Reading'}

# clear()
person.clear()
print(person)  # Output: {}
