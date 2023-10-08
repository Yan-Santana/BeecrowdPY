'''
- Tesoura corta papel
- Papel cobre pedra
- Pedra derruba lagarto
- Lagarto adormece Spock
- Spock derrete tesoura
- Tesoura prende lagarto
- Lagarto come papel
- Papel refuta Spock
- Spock vaporiza pedra
- Pedra quebra tesoura
'''

resultado = [
    ["empate", "sheldon", "rajesh", "rajesh", "sheldon"],
    ["rajesh", "empate", "sheldon", "sheldon", "rajesh"],
    ["sheldon", "rajesh", "empate", "rajesh", "sheldon"],
    ["sheldon", "rajesh", "sheldon", "empate", "rajesh"],
    ["rajesh", "sheldon", "rajesh", "sheldon", "empate"]
]
def pos(jogada):
    if jogada == "pedra":
        return 0
    elif jogada == "papel":
        return 1
    elif jogada == "tesoura":
        return 2
    elif jogada == "lagarto":
        return 3
    else:
        return 4
t = int(input())
for i in range(t):
    Rajesh, Sheldon = input().split()
    print(resultado[pos(Rajesh)][pos(Sheldon)])