import subprocess

def main():
    # Prompt user for the domain name
    domain = input("Enter domain: ")
    
    # Prompt user for the output file name (without extension)
    output_file_name = input("Enter the output file name (without extension): ")
    
    # Define the output file path
    output_file_path = f"/home/kali/Desktop/hackhound/Results/Reconnaissance_Results/{output_file_name}.txt"
    
    # Run the whois command and display the output in the terminal
    command = ["nmap", "--script", "hostmap-crtsh", domain]
    print(f"Running command: {' '.join(command)}")
    
    try:
        # Run the command and print the output directly
        result = subprocess.run(command, text=True, check=True)
        
        # Capture the output of the whois command
        whois_output = subprocess.run(command, capture_output=True, text=True, check=True).stdout
        
        # Write the output to the specified file
        with open(output_file_path, 'w') as file:
            file.write(whois_output)
        
        print(f"Output saved to {output_file_path}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error running whois command: {e}")

if __name__ == "__main__":
    main()
