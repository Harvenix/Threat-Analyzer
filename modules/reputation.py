import re
import requests
from core import api_manager
from rich.console import Console
from rich.table import Table

console = Console()

def run_reputation_check():
    """Gets user input and calls the appropriate analysis function."""
    console.print("\n[bold]--- IOC Reputation Analysis ---[/]")
    user_input = console.input("[bold]Enter an IP Address to analyze: [/]").strip()

    ip_regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    if re.match(ip_regex, user_input):
        analyze_ip(user_input)
    else:
        console.print("[bold red][!] Invalid input. Please enter a valid IP address.[/]")

def analyze_ip(ip):
    """Analyzes an IP address using VirusTotal and displays a rich table."""
    api_key = api_manager.API_KEYS.get('VirusTotal')
    if not api_key:
        console.print("[bold red][!] VirusTotal API Key not configured.[/]")
        return
    
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": api_key}
    
    with console.status(f"[bold green]Analyzing IP: {ip}...[/]") as status:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json().get('data', {}).get('attributes', {})
            stats = data.get('last_analysis_stats', {})
            malicious = stats.get('malicious', 0)
            
            table = Table(title=f"VirusTotal Report for [cyan]{ip}[/]")
            table.add_column("Attribute", style="magenta", no_wrap=True)
            table.add_column("Value", style="white")

            table.add_row("Owner", data.get('as_owner', 'N/A'))
            table.add_row("Country", data.get('country', 'N/A'))
            
            detection_style = "red" if malicious > 0 else "green"
            table.add_row(f"[{detection_style}]Malicious Detections[/]", f"[{detection_style}]{malicious}[/]")

            console.print(table)
            
        except requests.RequestException:
            console.print(f"[bold red][!] Error fetching report for IP: {ip}[/]")