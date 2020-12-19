import os
from colorama import Fore, Back, Style


def clear():
    os.system('cls')

clear()

def start():
    clear()
    print(Fore.BLUE + "███████╗██╗  ██╗███████╗██╗     ██╗         ███╗   ██╗ █████╗ ███╗   ███╗███████╗")
    print(Fore.BLUE + "██╔════╝██║  ██║██╔════╝██║     ██║         ████╗  ██║██╔══██╗████╗ ████║██╔════╝")
    print(Fore.BLUE + "███████╗███████║█████╗  ██║     ██║         ██╔██╗ ██║███████║██╔████╔██║█████╗  ")
    print(Fore.BLUE + "╚════██║██╔══██║██╔══╝  ██║     ██║         ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ")
    print(Fore.BLUE + "███████║██║  ██║███████╗███████╗███████╗    ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗")
    print(Fore.BLUE + "╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
prefix = "</>"


def system_it():
    print("CIAO")
    while True:
        
        global prefix
        script = input(Fore.GREEN + prefix) 
        if script == "comandi" or script == "help":
            clear()
            comandi = "Commandi: \nhelp / comandi - lista comandi \nripeti - ripete ciò che vuoi \nprefisso - permette di cambiare il prefisso \nping - scoprilo :) \nlang - cambia lingua"
            print(comandi)
        elif script == "ripeti":
            repeat = input("Cosa devo ripetere? ")
            clear()
            print(repeat)
        elif script == "prefisso":
            prefix = input("Nuovo prefisso = ")
            clear()
        elif script == "ping":
            clear()
            print("Pong")
        elif script == "lang":
            lang()
        else:
            clear()
            print(Style.RESET_ALL + Fore.RED + script + ' ' + Style.RESET_ALL + Style.RESET_ALL + "Errore: comando non valido" + Style.RESET_ALL)
         



def system_en():
    print("HIIIII")
    while True:
        
        global  prefix
        script = input(Fore.GREEN + prefix)
        if script == "help":
            clear()
            comandi = "Commands: \nrepeat \nprefix \nping \nlang"
            print(comandi)
        elif script == "repeat":
            repeat = input("What i should repeat? ")
            clear()
            print(repeat)
        elif script == "prefix":
            prefix = input("New prefix = ")
            clear()
        elif script == "ping":
            clear()
            print("Pong")
        elif script == "lang":
            lang()
        
        else:
            clear()
            print(Style.RESET_ALL + Fore.RED + script + ' ' + Style.RESET_ALL + Style.RESET_ALL + "Error: command not found" + Style.RESET_ALL)
            
        
def lang():
    scelta = input("Write 'ita' to go in italian mode, write 'eng' to go in english mode ")
    if scelta == "ita":
        system_it()
    elif scelta == "eng":
        system_en()
    else:
        print("This language isn't supported")
        lang()
start()
lang()

