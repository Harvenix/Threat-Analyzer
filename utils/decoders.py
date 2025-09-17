import base64
import urllib.parse

def run_decoders():
    """Displays menu for URL decoding utilities."""
    print("\n--- URL Decoder ---")
    print("  1) Standard URL Decode (for things like %20)")
    print("  2) Base64 Decode")
    choice = input(">> Select a decoder type: ")
    url = input("Enter the text/URL to decode: ").strip()

    if choice == '1':
        decoded = urllib.parse.unquote(url)
        print(f"\n[+] Decoded URL: {decoded}")
    elif choice == '2':
        try:
            decoded = base64.b64decode(url).decode()
            print(f"\n[+] Decoded Text: {decoded}")
        except Exception as e:
            print(f"[!] Invalid Base64 text. Error: {e}")
    else:
        print("[!] Invalid choice.")