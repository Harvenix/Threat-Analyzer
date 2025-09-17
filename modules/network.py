from ipwhois import IPWhois
import socket
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_network_tools():
    """Displays menu for network tools."""
    console.print("\n[bold]--- Network Tools ---[/]")
    console.print("  [cyan]1[/]) DNS Lookup (Get IP from domain)")
    console.print("  [cyan]2[/]) WHOIS Lookup (Get owner info for an IP)")
    choice = console.input("[bold]>> Select an option: [/]")
    
    if choice == '1':
        dns_lookup()
    elif choice == '2':
        whois_lookup()
    else:
        console.print("[bold red][!] Invalid option.[/]")

def dns_lookup():
    """Performs a DNS lookup to find an IP address for a domain."""
    domain = console.input("Enter the domain name (e.g., google.com): ").strip()
    try:
        ip_address = socket.gethostbyname(domain)
        console.print(Panel(
            f"The IP address for [cyan]{domain}[/] is [bold green]{ip_address}[/]",
            title="[bold blue]DNS Lookup Result[/]",
            border_style="blue"
        ))
    except socket.gaierror:
        console.print(f"[bold red][!] Could not find an IP for {domain}.[/]")

def whois_lookup():
    """Performs a WHOIS lookup to find ownership info for an IP."""
    ip = console.input("Enter the IP address: ").strip()
    try:
        with console.status(f"[bold green]Performing WHOIS lookup for {ip}...[/]"):
            obj = IPWhois(ip)
            results = obj.lookup_whois()
            
            description = results.get('nets', [{}])[0].get('description', 'N/A').strip()
            country = results.get('nets', [{}])[0].get('country', 'N/A')
            
            report = f"[bold]Description:[/] {description}\n[bold]Country:[/] {country}"
            console.print(Panel(report, title=f"[bold blue]WHOIS Report for {ip}[/]", border_style="blue"))
            
    except Exception:
        console.print(f"[bold red][!] Could not get WHOIS information for {ip}.[/]")