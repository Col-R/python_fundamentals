#Similar to arrays in JS
#Indexed starting in 0
ninjas = ['Ryu', 'Scorpion', 'Ibuki']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

# In Python, the elements of a list do not have to be of the same data type
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# accessing values
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

# manipulating lists
x = [1,2,3,4,5]
x.append(99)
print(x)

# Python uses [ ] characters to return a copy of the list, constrained to the specified indices
x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];

# list built in functions
    # len(sequence): Returns the number of items in a sequence.
my_list = [1, 'Zen', 'hi']
print(len(my_list))

    #list.append(value)
my_list = [1,5,2,8,4]
my_list.append(7)
print(my_list)
# output:
# [1,5,2,8,4,7]



# enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence
