# basic question
for i in range(151):
    print(i)

# Multiples of five
for i in range(5, 1001, 5):
    print(i)

# counting, the dojo way
for i in range(0, 101):
    if i % 10 == 0:
        print('Coding Dojo')

    elif i % 5 == 0:
        print('Coding')

    else:
        print(i)

# Whoa. That sucker's huge
for i in range(0, 500000):
    if i % 2 == 1:
        print(i)

# countdown by fours
for i in range (2018, 0, -4):
    print(i)

# flexible counter
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)




