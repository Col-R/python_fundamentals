num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #data types, boolean
string = 'Hello World' #data type, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #data type, composite, list, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#data type, compostie, dict, initialize
fruit = ('blueberry', 'strawberry', 'banana') #data type, composite, tuple, initialize
print(type(person)) #type check
print(pizza_toppings[1]) #list, access value, log
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #dictionary, access value, log statement
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary. add value
print(fruit[2]) #tuple, access value, log

if num1 > 45:
    print("It's greater") #conditional
else:
    print("It's lower") #

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1



pizza_toppings.pop() #delete value from dict
pizza_toppings.pop(1)

print(person)
person.pop('eye_color') # delete value from dict
print(person)

for topping in pizza_toppings: #while loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function
    for num in range(10): #for loop argument
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)#function call with paramnter

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
