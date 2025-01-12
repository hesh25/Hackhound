import subprocess
import re
from rich.console import Console
from rich.table import Table
import os

def get_domain():
    return input("Enter the domain: ")

def get_output_filename():
    filename = input("Enter the output file name (without extension): ")
    return f"/home/kali/Desktop/hackhound/Results/Portscan_Results/{filename}.txt"

def run_nmap_scan(domain, output_file):
    nmap_command = ["nmap", "-vv", "-sT", domain, "-oN", output_file]
    subprocess.run(nmap_command)
    return output_file

def parse_nmap_results(file_path):
    open_ports = []
    with open(file_path, 'r') as file:
        for line in file:
            # Match lines that indicate an open port and capture details
            match = re.match(r'(\d+/(tcp|udp))\s+(open)\s+(\S+)\s+(.*)', line)
            if match:
                port = match.group(1)
                state = match.group(3)
                service = match.group(4)
                reason = match.group(5)
                open_ports.append((port, state, service, reason))
    return open_ports

def save_table_to_file(table, file_path):
    console = Console(record=True)
    console.print(table)
    with open(file_path, 'a') as file:  # Append the table to the file
        file.write(console.export_text())

def main():
    domain = get_domain()
    output_file = get_output_filename()
    run_nmap_scan(domain, output_file)
    open_ports = parse_nmap_results(output_file)
    
    # Create and configure the table
    table = Table(title="Nmap Scan Results")

    # Add columns with green column names
    table.add_column("Open Ports", style="green")
    table.add_column("State", style="green")
    table.add_column("Service", style="green")
    table.add_column("Reason", style="green")

    for port, state, service, reason in open_ports:
        table.add_row(port, state, service, reason)
    
    # Save the table to the file
    save_table_to_file(table, output_file)

if __name__ == "__main__":
    main()
