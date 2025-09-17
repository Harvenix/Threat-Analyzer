import webbrowser
import os
from utils import file_handler

def run_phishing_kit():
    """Displays menu for the phishing analysis toolkit."""
    print("\n--- Phishing Investigation Kit ---")
    print("  1) Analyze an Email Attachment")
    print("  2) Show Phishing Identification Guide")
    choice = input(">> Select an option: ")
    if choice == '1':
        analyze_attachment()
    elif choice == '2':
        show_phishing_guide()
    else:
        print("[!] Invalid option.")

def analyze_attachment():
    """Gets a file hash and sends it for reputation analysis."""
    print("\nPlease select the suspicious file from the window that pops up.")
    from modules import reputation
    file_hash = file_handler.get_file_md5_hash()
    if file_hash:
        reputation.analyze_hash(file_hash)

def show_phishing_guide():
    """Opens the phishing guide image."""
    guide_path = 'phishing_guide.png'
    print(f"\n[+] Trying to open the guide: {guide_path}")
    try:
        if os.path.exists(guide_path):
            webbrowser.open(guide_path)
        else:
            print(f"[!] Error: The picture '{guide_path}' was not found in your ThreatAnalyzer folder.")
    except Exception as e:
        print(f"[!] An error occurred while trying to open the image: {e}")