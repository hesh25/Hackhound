import subprocess
import re
from rich.console import Console
from rich.table import Table

def get_domain():
    return input("Enter the domain: ")

def get_output_filename():
    filename = input("Enter the output file name (without extension): ")
    return f"/home/cb013204/Desktop/hackhound111/Results/{filename}.txt"

def run_nmap_scan(domain, output_file):
    nmap_command = ["sudo", "nmap", "-vv", "-sV", "-ff", "--script", "ftp*", domain, "-v", "-oN", output_file]
    subprocess.run(nmap_command)
    return output_file

def parse_nmap_results(file_path):
    open_ports = []
    current_port = None
    vulnerabilities = []

    with open(file_path, 'r') as file:
        for line in file:
            # Match lines that indicate an open port and capture details
            port_match = re.match(r'(\d+/(tcp|udp))\s+(open)\s+(\S+)\s+(.*)', line)
            if port_match:
                if current_port:
                    # Append the current port with vulnerabilities or a "-" if none found
                    if vulnerabilities:
                        open_ports.append((current_port[0], current_port[1], current_port[2], "\n".join(vulnerabilities)))
                    else:
                        open_ports.append((current_port[0], current_port[1], current_port[2], "-"))
                    vulnerabilities = []

                port = port_match.group(1)
                state = port_match.group(3)
                service = port_match.group(4)
                current_port = (port, state, service)

            # Match lines that indicate a vulnerability detail
            vuln_match = re.match(r'\|_(.*)', line)
            if vuln_match and current_port:
                vulnerabilities.append(vuln_match.group(1).strip())

        # Append the last port with vulnerabilities or a "-" if none found
        if current_port:
            if vulnerabilities:
                open_ports.append((current_port[0], current_port[1], current_port[2], "\n".join(vulnerabilities)))
            else:
                open_ports.append((current_port[0], current_port[1], current_port[2], "-"))

    return open_ports

def determine_criticality(service):
    if "http" in service or "https" in service:
        return "High"
    elif "ftp" in service:
        return "Medium"
    elif "ssh" in service:
        return "Low"
    else:
        return "Critical"

def get_criticality_color(criticality):
    if criticality == "Low":
        return "white"
    elif criticality == "Medium":
        return "blue"
    elif criticality == "High":
        return "yellow"
    elif criticality == "Critical":
        return "red"

def save_table_to_file(table, file_path):
    console = Console(record=True)
    console.print(table)
    with open(file_path, 'a') as file:
        file.write(console.export_text())

def main():
    domain = get_domain()
    output_file = get_output_filename()
    run_nmap_scan(domain, output_file)
    open_ports = parse_nmap_results(output_file)
    
    table = Table(title="Nmap Scan Results")
    
    table.add_column("Open Ports", style="green")
    table.add_column("State", style="green")
    table.add_column("Service", style="green")
    table.add_column("Vulnerability", style="green")
    table.add_column("Criticality")

    for port, state, service, vulnerability in open_ports:
        criticality = determine_criticality(service)
        criticality_color = get_criticality_color(criticality)
        table.add_row(port, state, service, vulnerability, f"[{criticality_color}]{criticality}[/{criticality_color}]")
        table.add_row("", "", "", "", "")  # Add empty row for spacing
    
    save_table_to_file(table, output_file)

if __name__ == "__main__":
    main()
