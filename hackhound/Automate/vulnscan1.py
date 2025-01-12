import subprocess
from fpdf import FPDF

def run_script(script_path):
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Script Outputs', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_script_output(self, script_index, output):
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Output of script {script_index + 1}:', 0, 1)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, output)

# List of scripts to run
scripts = [
    '/home/kali/Desktop/hackhoulnd/Automate/whois1.py',
    '/home/kali/Desktop/hackhoulnd/Automate/portscan1.py',
    '/home/kali/Desktop/hackhoulnd/Automate/vulnscan1.py',
    '/home/kali/Desktop/hackhoulnd/Automate/hydra1.py',
    '/home/kali/Desktop/hackhoulnd/Automate/ffuf1.py',
    '/home/kali/Desktop/hackhoulnd/Automate/idor1.py'
]

results = []
for script in scripts:
    output = run_script(script)
    results.append(output)

pdf = PDF()
for i, result in enumerate(results):
    pdf.add_script_output(i, result)

output_path = "results.pdf"
pdf.output(output_path)

print(f"PDF created successfully at {output_path}")
