# Sentença Dançante

while True:
    try:
        entrada = input()
    except EOFError:
        break
    para_MA = True

    dancante = ""
    for i in range(len(entrada)):
        caracter = entrada[i]

        if caracter == " ":
            dancante += " "
        elif 65 <= ord(caracter) <= 90: #Se é maiusculo
            if para_MA == True:
                dancante += caracter
            else:
                dancante += chr(ord(caracter) +32)
            para_MA = not para_MA
        else:
            if para_MA == True:
                dancante += chr(ord(caracter) - 32)
            else:
                dancante += caracter
            para_MA = not para_MA
    print(dancante)
