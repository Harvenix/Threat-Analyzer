import re

def defang_ioc(ioc):
    """Replaces dots and protocols to make an IOC non-clickable."""
    ioc = re.sub(r'\.', '[.]', ioc)
    ioc = re.sub(r'http', 'hxxp', ioc)
    return ioc

def run_sanitizer():
    """Displays menu for sanitizing IOCs."""
    print("\n--- IOC Sanitizer (Defang) ---")
    ioc_input = input("Enter the IOC (IP, domain, URL) to sanitize: ").strip()
    sanitized_ioc = defang_ioc(ioc_input)
    print(f"\n[+] Sanitized IOC: {sanitized_ioc}")