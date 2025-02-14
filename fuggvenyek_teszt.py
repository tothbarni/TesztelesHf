import fuggvenyek

import os
os.system('CLS')

Y = "\033[33m"
B = "\033[1m"
C = "\033[36m"
G = "\033[32m"
R = "\033[31m"
X = "\033[0m"

def sorta_sum_teszt():
    a_lista = [3, 9, 10, 12, -3, 4, 4, 14, 14]
    b_lista = [4, 4, 11, -3, 12, 5, 6, 7, 6]
    vart_lista = [7, 20, 21, 9, 9, 9, 20, 21, 20]

    for i in range(len(a_lista)):
        print(f"{Y}{B}{i+1}. teszteset:{X}")
        a = a_lista[i]
        b = b_lista[i]
        vart = vart_lista[i]
        kapott = fuggvenyek.sorta_sum(a, b)

        if vart == kapott:
            eredmeny = f"{B}{G}OK{X}"
        else:
            eredmeny = f"{B}{R}HIBA{X}"

        print(f"{C}a: {a} | b: {b} |{X} várt összeg: {vart} | kapott: {kapott} | eredmény: {eredmeny}\n")

sorta_sum_teszt()
