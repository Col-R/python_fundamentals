# A tuple is kind of like an object. Has multiple values tied to one variable
# Cannot be modified or changed.

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(dog[2])
dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment

# we can add and slice tuples. See example below
dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

# Built in tuple functions:
x = (1,5,6,9,2)
print(len(x))
# output:
# 5
