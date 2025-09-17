import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from core import api_manager
from modules import reputation, network

def display_header():
    """Displays the main header for the application using Rich."""
    console = Console()
    console.print(Panel(
        "[bold cyan]Threat Analyzer[/] - [italic]Your Cyber Intelligence Toolkit[/]",
        title="[bold green]Welcome[/]",
        border_style="green"
    ))

def main_menu():
    """Displays the main menu and handles user input."""
    console = Console()
    console.print("\n[bold]--- Main Menu ---[/]")
    console.print("  [cyan]1[/]) Analyze an IOC (IP, URL, Hash)")
    console.print("  [cyan]2[/]) Network Tools (DNS, WHOIS)")
    console.print("  [cyan]8[/]) Configure API Keys")
    console.print("  [cyan]0[/]) Exit")

    choice = Prompt.ask("[bold]>> Select an option[/]", choices=["1", "2", "8", "0"], default="1")
    return choice

def main():
    """Main function to run the Threat Analyzer application."""
    display_header()
    time.sleep(1)

    try:
        api_manager.load_api_keys()
        if not api_manager.API_KEYS:
             raise FileNotFoundError
    except FileNotFoundError:
        console = Console()
        console.print("[yellow]Welcome! Let's set up your API keys first.[/yellow]")
        api_manager.configure_api_keys()
        api_manager.load_api_keys()

    while True:
        choice = main_menu()
        if choice == '1':
            reputation.run_reputation_check()
        elif choice == '2':
            network.run_network_tools()
        elif choice == '8':
            api_manager.configure_api_keys()
        elif choice == '0':
            console = Console()
            console.print("\n[bold magenta]Exiting Threat Analyzer. Stay safe![/]")
            break
        
        Prompt.ask("\n[dim]Press Enter to return to the menu...[/]")


if __name__ == "__main__":
    main()