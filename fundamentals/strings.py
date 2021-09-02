#string literals
print('this is a sample string')

#concatenation - The print() function inserts a space between elements separated by a comma.
name = "Zen"
print("My name is", name)
#The second is by concatenating the contents into a new string, with the help of +.
name = "Zen"
print("My name is " + name)

number = 5
print('My number is', number)
# print('My number is'+ number) throws an error

# Type Casting or Explicit Type Conversion

# print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
# total = total + user_val		 output: TypeError
total = total + int(user_val)		# total will be 61

# f-strings: Python 3.6 introduced f-strings for string interpolation. To construct a f-string, place an f right before the opening quotation. Then within the string, place any variables within curly brackets.
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

# string.format() Prior to f-strings, string interpolation was accomplished with the .format() method.
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
# %-formatting - an even older method, the % symbol is used to indicate a placeholder, a %s for a string and %d for a number.
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# Built in methods
x = "hello world"
print(x.title())
# output:
"Hello World"
