# 1 - Update values in dictionaries and lists
# 1.1 - Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x = [ [5,2,3], [10,8,9] ]

def listUpdate():
    list = x[1]
    list.remove(10)
    list.insert(0,15)
    return(list)
print (listUpdate())
print (x)

# 1.2 - Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def studentUpdate():
    students[0]['last_name'] = 'Bryant'
studentUpdate()
print (students)

# 1.3 - In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def sportUpdate():
    sports_directory['soccer'][0] = 'Andres'
sportUpdate()
print(sports_directory)

# 1.4 - Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

def zUpdate():
    z[0]['y'] = 30
zUpdate()
print(z)

# 2 - Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for x in range(len(students)):
        for key in students[x]:
            if key == 'first_name':
                print('first_name - ' + students[x][key])
            else:
                print('last_name - ' + students[x][key])
iterateDictionary(students)

# 3 - Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, some_list):
    values = [name[key_name] for name in some_list]
    print(values)
iterateDictionary2('last_name', students)



















#end
