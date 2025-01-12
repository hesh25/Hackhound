import subprocess

def run_whois():
    subprocess.call(["python3", "Reconnaissance/whois.py"])

def run_dnsbrute():
    subprocess.call(["python3", "Reconnaissance/dnsbrute.py"])

def run_hostmap():
    subprocess.call(["python3", "Reconnaissance/hostmap.py"])

def run_exit():
    subprocess.call(["python3", "hackhound1.py"])    

def main():
    while True:
        print("""
                    _______________________________________________ 
                    |       \033[1;91m Reconnaissance     \033[1;m                  |
                    |1-) Whois                                    |
                    |2-) DNS Brute-force Hostnames                |
                    |3-) Subdomain/hostmap-crtsh                  |
                    |_____________________________________________|

                    0-) Exit
        """)
        
        option = input("Enter your choice: ")
        
        if option == "1":
            run_whois()
        elif option == "2":
            run_dnsbrute()
        elif option == "3":
            run_hostmap()
        elif option == "0":
            run_exit()
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
