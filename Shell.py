import os
from colorama import Fore, Back, Style



def clear():
    os.system('cls')

clear()



def start():
    clear()
    print(Fore.BLUE + '''    ███████╗██╗  ██╗███████╗██╗     ██╗         ███╗   ██╗ █████╗ ███╗   ███╗███████╗
    ██╔════╝██║  ██║██╔════╝██║     ██║         ████╗  ██║██╔══██╗████╗ ████║██╔════╝
    ███████╗███████║█████╗  ██║     ██║         ██╔██╗ ██║███████║██╔████╔██║█████╗  
    ╚════██║██╔══██║██╔══╝  ██║     ██║         ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
    ███████║██║  ██║███████╗███████╗███████╗    ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝''')
    #YOU CAN FIND THIS TEXT ON https://fsymbols.com/generators/carty/ OR ON http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=
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

    if scelta == "ita":
        system_it()
        
    elif scelta == "eng":
        system_en()
        
    else:
        print("This language isn't supported")
        lang()


def credits():
    print("")
    
    file_l = open("not_modify/c.txt", "r").read()
        
    if file_l == "accept":
        
    
        start()
        lang()
        file_l.close()
        
    else:
        if scelta == 'eng':

            print(Fore.MAGENTA + '''This Shell was created by Lorix.
You can't use this for commercial purposes.
You can modify him ONLY for personal purposes.
If you have any questions contact me on Instagram, the link is in the README.md file.''')
            accepting = input("Do you accept these conditions? If yes write 'accept' else press 'ENTER' ")
            if accepting == "accept":
                file_s = open("not_modify/c.txt", "w")
                file_s.write("accept")
                file_s.close()
                start()
                lang()
            else:
                print("Sorry, you can't use this Shell.")
        elif scelta == 'ita':
            print(Fore.MAGENTA +'''Questa Shell è stata creata da Lorix.
Non puoi usarla per scopi commerciali.
Puoi modificarla SOLO per scopi personali.
Se hai domande contattami su Instagram, il link si trova nel file README.md.''')
            accetti = input("Accetti queste condizioni? Se sì scrivi 'accetto' altrimenti premi 'INVIO' ")
            if accetti == "accetto":
                file_s = open("not_modify/c.txt", "w")
                file_s.write("accept")
                file_s.close()
                start()
                lang()
            else:
                print("Mi dispiace, non puoi usare questa Shell.")
        else:
            print("This language isn't supported")

            

scelta = input(Fore.YELLOW + "Write 'ita' to go in italian mode, write 'eng' to go in english mode ")

credits()
if scelta == 'ita':
    input("Qualcosa è andato storto...")
if scelta == 'eng':
    input("Something went wrong...")