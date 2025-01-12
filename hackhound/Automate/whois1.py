import subprocess

def main():
    # Prompt user for the domain name
    domain = input("Enter domain: ")
    
    # Prompt user for the output file name (without extension)
    output_file_name = input("Enter the output file name (without extension): ")
    
    # Define the output file path
    output_file_path = f"/home/kali/Desktop/hackhound/Results/Reconnaissance_Results/{output_file_name}.txt"
    
    # Run the whois command and display the output in the terminal
    command = ["whois", domain]
    print(f"Running command: {' '.join(command)}")
    
    try:
        # Run the command and print the output directly
        result = subprocess.run(command, text=True, check=True)
    
    except subprocess.CalledProcessError as e:
        print(f"Error running whois command: {e}")

if __name__ == "__main__":
    main()
