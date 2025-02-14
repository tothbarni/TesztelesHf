import fuggvenyek
from colorama import Fore, Style
import os
os.system('CLS')

def sorta_sum_teszt():
    a_lista = [3, 9, 10, 12, -3, 4, 4, 14, 14]
    b_lista = [4, 4, 11, -3, 12, 5, 6, 7, 6]
    vart_lista = [7, 20, 21, 9, 9, 9, 20, 21, 20]

    for i in range(0, len(a_lista), 1):
        print(f"{Fore.YELLOW}{Style.BRIGHT}{i+1}. teszteset:{Style.RESET_ALL}")
        a:int=a_lista[i]
        b:bool=b_lista[i]
        vart:bool=vart_lista[i]
        kapott:bool=fuggvenyek.sorta_sum(a, b)
        if (vart==kapott):
            eredmeny=f"{Style.BRIGHT}{Fore.GREEN}OK{Fore.RESET}"
        else:
            eredmeny=f"{Style.BRIGHT}{Fore.RED}HIBA{Fore.RESET}"
        print(f"{Fore.CYAN}a: {a} | b: {b} |{Fore.RESET} várt összeg: {vart} | kapott: {kapott} | eredmény: {eredmeny}\n")

sorta_sum_teszt()