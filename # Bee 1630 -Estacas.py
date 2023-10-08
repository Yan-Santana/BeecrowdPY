""""""""""
from math import gcd

while True:
    try:
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
    except EOFError:
        break
    if int(xy[0]) == int(xy[1]):
        print(4)
    else:
        m = gcd(int(xy[0]), int(xy[1]))
        print((int(xy[0]) // m)*2 + (int(xy[1]) // m)*2)
"""""""""
"""""""""
def mdc(num1, num2):
    resto = None
    while resto != 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    return num1

while True:
    try:
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
    except EOFError:
        break
    if x == y:
        print(4)
    else:
        m = mdc(x, y)
        print((x // m)*2 + (y // m)*2)
"""""""""

while True:
    try:
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
    except EOFError:
        break

    if x == y:
        print(4)

    else:
        while x < y and y % x or y < x and x % y:
          if x < y:
              y -= x
        else:



        m = int(y)
    print((x // m)*2 + (y // m)*2)