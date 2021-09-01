x = 10
if x > 50:
	print("bigger than 50")
else:
	print("smaller than 50")

class EmptyClass:
    pass
# Python has provided us with the pass statement for situations where we know we need the block statement, but we aren't sure what to put in it yet.
for val in my_string:
    pass
# The pass statement is a null operation; nothing happens when it executes. The pass is almost never seen in final production, but can be useful in places where your code has not been completed yet.

# Data Types

    # Boolean
    is_hungry = True
    has_freckles = False

    # Numbers
    age = 35 # storing an int
    weight = 160.57 # storing a float

    # Strings
    name = "joe blue"

# Composite types
    # Tuples
    dog = ('Bruce', 'cocker spaniel', 19, False)
    print(dog[0])		# output: Bruce
    dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

    # Lists
    empty_list = []
    ninjas = ['Rozen', 'KB', 'Oliver']
    print(ninjas[2]) 	# output: Oliver
    ninjas[0] = 'Francis'
    ninjas.append('Michael')
    print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
    ninjas.pop()
    print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
    ninjas.pop(1)
    print(ninjas)	# output: ['Francis', 'Oliver']

    # Dictionaries
    empty_dict = {}
    new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
    new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
    new_person['hobbies'] = ['climbing', 'coding']
    print(new_person)
    # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
    w = new_person.pop('weight')	# removes the specified key and returns the value
    print(w)		# output: 160.2
    print(new_person)
    # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

# Common Functions
    # If we're ever unsure of a value or variable's data type, we can use the type function to find out.
    print(type(2.63))		# output: <class 'float'>
    print(type(new_person))		# output: <class 'dict'>

    # For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:
    print(len(new_person))		# output: 4 (the number of key-value pairs)
    print(len('Coding Dojo'))	# output: 11
