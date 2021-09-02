# 1 - Basic
for x in range(0,151):
    print (x)

# 2 - Multiples of Five
for i in range(5,1001, 5):
    print (i)

# 3 - Counting the Dojo Way
for n in range (1,101):
    if n%10 == 0:
        print('Coding Dojo')
    elif  n%5 == 0:
        print('Coding')
    else:
        print(n)

#4 - Big Number
big = 0
for a in range(500000):
    if a%2 != 0:
        big = big + a
print (big)

# 5 - Countdown by Fours
year = 2018
while year > 0:
    print(year)
    year -=4

# 6 - Flexible counter
lowNum = 6
highNum = 20
mult = 5

for y in range (lowNum, highNum+1):
    if y%mult == 0:
        print(y)
