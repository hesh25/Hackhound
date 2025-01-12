import subprocess

def run_defaultscan():
    subprocess.call(["python3", "Portscan/defaultscan.py"])

def run_advancedscan():
    subprocess.call(["python3", "Portscan/advancedscan.py"])

def run_hostdiscovery():
    subprocess.call(["python3", "Portscan/hostdiscovery.py"])

def run_synscan():
    subprocess.call(["python3", "Portscan/synscan.py"])

def run_tcpscan():
    subprocess.call(["python3", "Portscan/tcpscan.py"])

def run_udpscan():
    subprocess.call(["python3", "Portscan/udpscan.py"])

def run_nullscan():
    subprocess.call(["python3", "Portscan/nullscan.py"])

def run_exit():
    subprocess.call(["python3", "hackhound1.py"])    

def main():
    while True:
        print("""
                    _______________________________________________ 
                    |\033[1;91m Default Scan Types \033[1;m                         |
                    |1-) Default Scan                             |
                    |2-) Advanced Scan                            |
                    |3-) Host Discovery                           |
                    |4-) Port(SYN) Scan                           |
                    |5-) Port(TCP) Scan                           |
                    |6-) Port(UDP) Scan                           |
                    |7-) Null scan (-sN)                          |
                    |_____________________________________________|

                    00-) Contact
                    0-) Exit
        """)
        
        option = input("Enter your choice: ")
        
        if option == "1":
            run_defaultscan()
        elif option == "2":
            run_advancedscan()
        elif option == "3":
            run_hostdiscovery()
        elif option == "4":
            run_synscan()
        elif option == "5":
            run_tcpscan()
        elif option == "6":
            run_udpscan()
        elif option == "7":
            run_nullscan()
        elif option == "0":
            run_exit()
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
