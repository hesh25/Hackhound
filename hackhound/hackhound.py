import subprocess
import socket
import os
import requests
import subprocess
import signal
import sys
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

banner = """
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░   ░░░░   ░░░░░░░░░░░░░░░░░░░░   ░░░░░░   ░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░
    ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒
    ▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒    ▒   ▒▒   ▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒   ▒▒   ▒   ▒   ▒▒▒▒▒▒▒▒   ▒
    ▓          ▓▓   ▓▓   ▓▓▓   ▓▓▓▓   ▓   ▓▓          ▓▓   ▓▓   ▓▓   ▓▓   ▓▓   ▓▓   ▓▓   ▓   ▓
    ▓   ▓▓▓▓   ▓   ▓▓▓   ▓▓   ▓▓▓▓▓     ▓▓▓▓   ▓▓▓▓   ▓   ▓▓▓▓   ▓   ▓▓   ▓▓   ▓▓   ▓  ▓▓▓   ▓
    ▓   ▓▓▓▓   ▓   ▓▓▓   ▓▓▓   ▓▓▓▓   ▓   ▓▓   ▓▓▓▓   ▓▓   ▓▓   ▓▓   ▓▓   ▓▓   ▓▓   ▓  ▓▓▓   ▓
    █   ████   ███   █    ████    █   ██   █   ████   ████   ███████      █    ██   ██   █   █
    ██████████████████████████████████████████████████████████████████████████████████████████

        ___________________________________________________________________________________
        |                                                                                 |
        |           < Automated Web Application Penetration Testing Tool >                |
        |                                                                                 |
        |_________________________________________________________________________________|
                              |   Developed by Techsafegaurd  |
                              | GitHub : XXXXXX               |
                              | Owner  :  APIIT               | 
                              |                               |
                              |_______________________________|
"""
print(color.BOLD,color.BLUE+banner+color.END)

menu = """
        [+] \033[4mChoose An Option\033[0m
                _______________________________________________________________
                | [1] Reconnaissance             |   [4] Exploitations        |
                | [2] Port-Scanner               |   [5] Post Exploitation    |
                | [3] Vulnerability-Scanner      |   [6] Automate All         |
                +-------------------------------------------------------------+
                |   [N] New Target        [X] Unistall        [E] Exit        |
                +-------------------------------------------------------------+

"""

def clear_terminal():
    os.system('clear')

def signal_handler(sig, frame):
    clear_terminal()
    sys.exit(0)

def ping():
        global domain
        global IP
        domain = input("Enter Target Address [Example.com / IP]: ")
        try:    
                IP = socket.gethostbyname(domain)
        except socket.gaierror or requests.ConnectionError:
                print("\n\033[0;31m[*] Invalid Target Address\033[0m\n")
                ping()
        else:   
                response = os.system("ping -c 1 " + domain)
                if response == 0:
                        print("\n\033[0;31m[-] Target is Live\033[0m")
                        
                else:
                        print("\n\033[0;31m[!] Oops!! Target is not Live\033[0m\n")
                        ping()

def Exit():
        while True :
                cond = input("Are you sure (y/n) : ")
                if cond == str('y'or 'Y'):
                        exit()  
                elif cond == str('n' or 'N'):
                        os.system("clear")
                        print(banner)
                        main()
                else:
                        print("\n\033[0;31m[!] Invalid Input\033[0m\n")

def run_reco():
    subprocess.run(["python3", "reconnaissance.py"])

def run_port_scan():
    subprocess.run(["python3", "portscan.py"])

def run_vulnerability_scan():
    subprocess.run(["python3","vulnerabilityscan.py"])

def run_exploitations():
    subprocess.run(["python3","exploitation.py"])

def run_post_exploitations():
    subprocess.run(["python3","HackHoundPE.py"])

def run_auto():
    subprocess.run(["python3", "automate.py"])

def main():
    while True:
        print(menu)
        choice = input("Choose an option: ")

        if choice == "1":
            run_reco()
        elif choice == "2":
            run_port_scan()
        elif choice == "3":
            run_vulnerability_scan()
        elif choice == "4":
            run_exploitations()
        elif choice == "5":
            run_post_exploitations()
        elif choice == "6":
            run_auto()
        elif choice == str('e' or 'E'):                   
            Exit() 
        elif choice == str('n' or 'N') :
            
            main()
        elif choice == str('x' or 'X') :
            while True :
                uni_cond = input("Are you sure (y/N) : ")
                if uni_cond == str('y' or 'Y'):
                        os.system("cd .. && rm -rf HackHound")
                elif uni_cond == str('n' or 'N'):                                                                                          
                        main()
                else:
                        print("\n\033[0;31m[!] Invalid Input\033[0m\n")

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    ping()
    main()
