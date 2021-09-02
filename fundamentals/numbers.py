#int
num = 10
#float
dec = 6.1
#log
print(num)
#type check
print (type(dec))
#conversion
num_to_dec = float(num)
#random number selector
import random
rand_num = random.randint(2,5)

# There are 3 basics types of numbers in Python.

# int - whole numbers, positive or negative.  ex. 35
# float - decimal numbers, positive or negative.  ex. 4.2
# complex - are a part of the real number system and are often referenced with the letter j.  ex. 1 + 3j.  **Note** If you're not sure if you need to use them, it's safe to say you can ignore this data type.

#type - use the type() to view the object type of any object.
print(type(24))
print(type(3.9))
print(type(3j))

#conversion - All Python objects have data type methods we can use to convert number types from one to another.
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#random
import random
print(random.randint(2,5)) # provides a random number between 2 and 5
