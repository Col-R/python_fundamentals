# 1 - Countdown Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(n):
    count = []
    while n>=0:
        count.append(n)
        n-=1
    return count
print (countdown(5))

# 2 - Print and Return Create a function that will receive a list with two numbers. Print the first value and return the second.
list = [1,2]
def print_and_return(num):
    for x in num:
        print (num[0])
        return (num[1])
print_and_return(list)

# 3 - First Plus Length Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
list = [1,2,3,4,5]
def first_plus_len(num):
    a = num[0]
    b = len(num)
    return a + b
print (first_plus_len(list))

# 4 - Values greater than Second: Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
list1 = [5,2,3,2,1,4]
def greater_than_second(num):
    list2 = []
    count_greater = 0
    second = list1[1]
    for x in num:
        if x > second:
            list2.append(x)
            count_greater += 1
    print(count_greater)
    return list2
print (greater_than_second(list1))

# 5 - This Length, That Value: Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_value(size, value):
    list = []
    x = 0
    while x < size:
        list.append(value)
        x += 1
    return list
print (length_value(7,-5))

#end
