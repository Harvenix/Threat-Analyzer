from cryptography.fernet import Fernet
import os
import sys
import ctypes
from rich.console import Console
from rich.prompt import Prompt

API_KEYS = {}
_API_KEY_FILENAME = 'api.ini'
_ENCRYPTION_KEY_FILE = 'analyzer.key'
# For this version, we only need VirusTotal to keep it simple and powerful.
_SERVICES = ['VirusTotal'] 

console = Console()

def _get_key_path():
    """Determines the correct path for the encryption key based on OS."""
    return '.' + _ENCRYPTION_KEY_FILE if sys.platform != 'win32' else _ENCRYPTION_KEY_FILE

def configure_api_keys():
    """Guides the user to enter and encrypt API keys."""
    console.print("\n[bold]--- API Key Configuration ---[/]")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    with open(_API_KEY_FILENAME, 'w') as f:
        for service in _SERVICES:
            api_key = Prompt.ask(f" -> Enter API key for [bold cyan]{service}[/]").strip()
            encrypted_key = cipher_suite.encrypt(api_key.encode()).decode()
            f.write(f"{service}:{encrypted_key}\n")
    
    key_path = _get_key_path()
    try:
        with open(key_path, 'w') as f:
            f.write(key.decode())
        if sys.platform == 'win32':
            ctypes.windll.kernel32.SetFileAttributesW(key_path, 2)
        console.print("\n[bold green][+] Configuration successful! API key is encrypted.[/]")

    except PermissionError:
        os.remove(key_path)
        console.print("\n[bold red][!] Permission Error: Could not write the encryption key.[/]")
        sys.exit(1)

def load_api_keys():
    """Loads and decrypts API keys into the global dictionary."""
    global API_KEYS
    key_path = _get_key_path()
    try:
        with open(key_path, 'r') as f:
            key = f.read().encode()
        cipher_suite = Fernet(key)
        with open(_API_KEY_FILENAME, 'r') as f:
            for line in f:
                if ':' in line:
                    service, encrypted_key = line.strip().split(':', 1)
                    decrypted_key = cipher_suite.decrypt(encrypted_key.encode()).decode()
                    API_KEYS[service] = decrypted_key
    except FileNotFoundError:
        API_KEYS = {}