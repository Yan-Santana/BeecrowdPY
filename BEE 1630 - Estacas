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
