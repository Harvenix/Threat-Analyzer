import hashlib
import tkinter as tk
from tkinter import filedialog

def get_file_md5_hash():
    """Opens a file dialog to select a file and returns its MD5 hash."""
    try:
        root = tk.Tk()
        root.withdraw() # Hide the main window
        file_path = filedialog.askopenfilename(title="Select a file to analyze")
        if not file_path:
            print("No file selected.")
            return None

        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)

        file_hash = hasher.hexdigest()
        print(f"\n[+] MD5 Hash of the file is: {file_hash}")
        return file_hash
    except Exception as e:
        print(f"[!] Could not process the file. Error: {e}")
        return None