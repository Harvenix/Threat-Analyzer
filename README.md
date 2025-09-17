# Threat Analyzer 🕵️‍♂️

**An interactive command-line toolkit for rapid cyber threat intelligence. Threat Analyzer transforms your terminal into a modern, powerful, and visually rich console for investigating IOCs.**

-----

## 🚀 About The Project

In the world of cybersecurity, speed and clarity are everything. **Threat Analyzer** was born from the need to escape the slow, multi-tab workflow of traditional threat analysis. Why juggle browser windows when you can have a powerful, centralized intelligence hub right in your terminal?

This tool leverages the Python **`rich`** library to create a stunning and intuitive Text User Interface (TUI). It goes beyond simple text, presenting complex data in beautifully formatted tables, panels, and progress bars. It's a command-line tool that doesn't feel like one—it's fast, efficient, and designed for the modern analyst.

<img width="1044" height="242" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/4f4880d4-9a0c-4a71-9af0-7fd0878eefe5" />


-----

## ✨ Core Features

  * 🎨 **Creative & Rich Interface:** A visually engaging terminal experience with colors, tables, and panels that make data easy to read and understand.
  * 📊 **IOC Reputation Analysis:** Instantly analyze the threat level of IP addresses using the **VirusTotal** API, with results displayed in a clean, professional table.
  * 🌐 **Essential Network Tools:** Perform quick **DNS** and **WHOIS** lookups to gather critical context about domains and IP ownership without leaving the interface.
  * 🔐 **Encrypted API Key Storage:** Your sensitive API keys are securely encrypted on your local machine, ensuring they are never exposed.
  * 🔧 **Clean & Modular Codebase:** The project is logically structured into `core` and `modules`, making it incredibly easy for you or others to contribute and add new features.

-----

## 🛠️ Getting Started

Get your local copy of Threat Analyzer up and running in a few simple steps.

### Prerequisites

  * **Python 3.8+** and **pip** must be installed on your system.
  * A **VirusTotal API Key** is required for IOC analysis.

### Installation & Launch

1.  **Clone the Repository**

    ```sh
    git clone https://github.com/Harvenix/Threat-Analyzer.git
    ```

2.  **Navigate to the Directory**

    ```sh
    cd Threat-Analyzer
    ```

3.  **Install Dependencies**

    ```sh
    pip install -r Requirements.txt
    ```

4.  **Launch the Tool\!**

    ```sh
    python threat_analyzer.py
    ```

    *On your first run, the tool will securely prompt you to enter your VirusTotal API key.*

-----

## 📖 How to Use

The tool operates through a simple interactive menu. Below are examples of the primary functions.

### Main Menu

Upon launching, you are presented with the main menu where you can select the desired action.

```
--- Main Menu ---
  1) Analyze an IOC (IP, URL, Hash)
  2) Network Tools (DNS, WHOIS)
  8) Configure API Keys
  0) Exit
>> Select an option: 1
```

### IOC Analysis

After selecting Option 1, you can enter an IP address. The tool will display a beautifully formatted table with the intelligence report from VirusTotal.

**Command:**

```
Enter an IP Address to analyze: 8.8.8.8
```

**Example Output:**

```
┌───────────────────────────────────────────────────────────┐
│        VirusTotal Report for 8.8.8.8                      │
├───────────────────┬───────────────────────────────────────┤
│ Attribute         │ Value                                 │
├───────────────────┼───────────────────────────────────────┤
│ Owner             │ Google LLC                            │
│ Country           │ US                                    │
│ Malicious Detections │ 0                                  │
└───────────────────┴───────────────────────────────────────┘
```

### Network Tools

Selecting Option 2 allows you to perform network lookups. For example, a WHOIS lookup provides ownership details for an IP address.

**Command:**

```
>> Select an option: 2
--- Network Tools ---
  1) DNS Lookup (Get IP from domain)
  2) WHOIS Lookup (Get owner info for an IP)
>> Select an option: 2
Enter the IP address: 1.1.1.1
```

**Example Output:**

```
┌───────────────────────────────────────────────────────────┐
│               WHOIS Report for 1.1.1.1                    │
├───────────────────────────────────────────────────────────┤
│ Description: APNIC and Cloudflare DNS Resolver project    │
│ Country:     AU                                           │
└───────────────────────────────────────────────────────────┘
```

-----

## 🗺️ Project Roadmap

This is the initial version of Threat Analyzer. Here are some of the exciting features planned for the future:

  * [ ] **Expanded IOC Support:** Add full analysis for URLs and File Hashes.
  * [ ] **More Integrations:** Connect with other essential APIs like **URLScan.io** and **AbuseIPDB**.
  * [ ] **Report Exporting:** Add a feature to save your analysis results to a clean `.txt` or `.md` file.
  * [ ] **Custom Theming:** Allow users to choose different color schemes for the interface.

-----

## 🙏 Acknowledgments

This tool wouldn't be possible without the incredible work of the following projects:

  * **[Rich](https://github.com/Textualize/rich):** For making beautiful terminal UIs possible in Python.
  * **[Requests](https://github.com/psf/requests):** For elegant and simple HTTP requests.
  * **[VirusTotal](https://www.virustotal.com/):** For providing a world-class threat intelligence API.

-----

## 📜 License

Distributed under the MIT License. See the `LICENSE` file for more information.

-----

## ✍️ Author

  * **Harvenix** - *Initial Work & Development* - [Harvenix](https://www.google.com/search?q=https://github.com/Harvenix/)
