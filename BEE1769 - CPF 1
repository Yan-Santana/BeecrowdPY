while True: 
    try:
        cpf = input().split('-') 
    except EOFError:
        break
    c=0
    d=10
    sc=0
    sd=0

    vrf1 = cpf[1][0] 
    vrf2 = cpf[1][1]  

    for i in cpf[0]:
        if i != ".":
            c += 1
            d -= 1

            sc += int(i)*c
            sd += int(i)*d

    if sc % 11 == 10:
        sc = 0
    else:
        sc %= 11

    if sd%11 == 10:
        sd = 0
    else:
        sd %= 11

    if vrf1 == str(sc) and vrf2 == str(sd):
        print("CPF valido")
    else:
        print("CPF invalido")
