from core import api_manager
import requests
import time

def run_brand_monitor():
    """Displays menu for brand monitoring."""
    print("\n--- Brand Monitoring ---")
    print("  1) Take a Screenshot of a Website")
    choice = input(">> Select an option: ")
    if choice == '1':
        capture_screenshot()
    else:
        print("[!] Invalid option.")

def capture_screenshot():
    """Submits a URL to URLScan.io to get a report and screenshot."""
    target_url = input("Enter the full URL to screenshot (e.g., https://google.com): ").strip()
    api_key = api_manager.API_KEYS.get('URLScan IO')
    if not api_key:
        print("[!] URLScan IO API Key not configured.")
        return

    print(f"\n[+] Submitting {target_url} to URLScan.io...")
    headers = {'Content-Type': 'application/json', 'API-Key': api_key}
    data = {'url': target_url, 'visibility': 'private'}
    try:
        response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, json=data)
        response.raise_for_status()
        scan_uuid = response.json().get('uuid')
        print(f"    Scan submitted successfully! Waiting for results...")

        time.sleep(20)

        result_url = f'https://urlscan.io/api/v1/result/{scan_uuid}/'
        result_response = requests.get(result_url)
        if result_response.status_code == 200:
            screenshot = result_response.json().get('task', {}).get('screenshotURL')
            print("\n--- URLScan.io Report ---")
            print(f"  Screenshot available at: {screenshot}")
        else:
            print("    Report is not ready yet. You can check the result later on urlscan.io.")

    except requests.RequestException as e:
        print(f"[!] Error submitting scan to URLScan.io: {e}")