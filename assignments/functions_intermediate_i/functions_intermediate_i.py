# 1 - Update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.1 - Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
list = x[1]
list.remove(10)
list.insert(0,15)
print(list)

# 1.2 - 
