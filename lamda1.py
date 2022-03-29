from itertools import filterfalse


remainder = lambda num: num % 2
print(remainder(5))


product = lambda x, y: x * y
print(product(2, 3))


def testFunction(num):
    print(num)
    return lambda x: x * num


result10 = testFunction(10)
result100 = testFunction(100)

print(result10)
print(result100)

print(result100(9))
print(result10(9))

# Same as testfunction
result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result100(9))
print(result10(9))


def myFunction(n):
    return lambda a: a * n


mydoubler = myFunction(2)
myTripler = myFunction(3)

print(mydoubler(11))
print(myTripler(11))


numbered_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbered_list))
print(filtered_list)


def addition(n):
    return n + n


numbers = [1, 2, 3, 4]
result = map(addition, numbers)

print(list(result))


result = list(map(lambda n: n + n, numbers))
print(result)

"""
import os
clear = lambda: os.system("cls")
clear()
"""