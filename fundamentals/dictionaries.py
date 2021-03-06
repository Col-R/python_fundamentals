# creating a dictionary
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# Accessing values
print(weekend["Sun"])
print(capitals["svk"])

# Removing values
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

#changing values
weekend['Sunday'] = 'S'
print(weekend)

# nested dictionaries
context = {
    'questions': [
        {'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        {'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        {'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        {'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

# yourDictionary.method() for methods
# .keys()
# .values()
# .items()
