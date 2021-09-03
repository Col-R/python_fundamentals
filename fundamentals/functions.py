# return vs print

# define a function
# def myFunction():
#     print('hello')

# call the function
# print(myFunction())

# Every function returns something

# def a():
#     return 5
# x = a()
# print(x + 10)

# Parameter vs argument
def introduction(name): # (name) parameter
    print(f'Hello, my name is {name}')
introduction('Col') #Col is argument

def introduction(name, food='ramen'):
    print(f'Hello, my name is {name} and I like {food}')
introduction('Col')

def introduction(food, name = "Col"):
    print(f'Hello, my name is {name} and I like {food}')
introduction('ramen')

def be_cheerful(name = 'mr. nibbles', repeat = 2):
    print(f'Good morning {name}\n' * repeat)

be_cheerful('Col-R')
be_cheerful()
be_cheerful(repeat=4, name='Zuko')
