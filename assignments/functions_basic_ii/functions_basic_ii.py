# 1 - Countdown
def countdown(n):
    count = []
    while n>=0:
        count.append(n)
        n-=1
    return count
print (countdown(5))

# 2 - Print and Return
list = [1,2]
def print_and_return(num):
    for x in num:
        print (num[0])
        return (num[1])
print_and_return(list)

# 3 - First Plus Length
list = [1,2,3,4,5]
def first_plus_len(num):
    a = num[0]
    b = len(num)
    return a + b
print (first_plus_len(list))    
