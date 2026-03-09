# GhostTrace

**GhostTrace** is a lightweight, stealthy input monitoring tool developed in Python. It is designed to demonstrate low-level system hooking, event-driven programming, and asynchronous data logging on Windows environments.

> [!IMPORTANT]
> **Educational Purpose Only**: This project was created to study cybersecurity patterns and system APIs. Unauthorized use of this tool on devices you do not own is strictly prohibited and may be illegal.

---

## 🚀 Key Features

* **Silent Execution**: Fully compatible with `.pyw` format and `PyInstaller` for background operation (no console window).
* **Intelligent Buffering**: Reduces Disk I/O impact by storing keystrokes in memory and flushing them only when specific thresholds or triggers (like `ENTER` or `TAB`) are met.
* **Contextual Logging**: Automatically separates input strings when focus-shifting keys are pressed, making it easier to distinguish between different input fields (e.g., Email vs. Password).
* **Data Integrity**: Implements `os.fsync()` and `flush()` to ensure logs are physically written to the disk, preventing data loss during unexpected system shutdowns.
* **Built-in Easter Egg**: Includes a hidden identification protocol (Windows API `MessageBox`) triggered by a specific hardcoded sequence.



## 🛠️ Technical Stack

* **Language**: Python 3.x
* **Libraries**: `pynput` (Input monitoring), `ctypes` (Native Windows API calls).
* **Packaging**: `PyInstaller` (Portable standalone executable).

## 📂 Project Structure

* `main.py`: The core logic and listener.
* `session_config.dat`: The encrypted/obfuscated log file (generated at runtime).
* `.gitignore`: Pre-configured to exclude sensitive logs and build artifacts.



## ⚙️ Setup & Deployment

1. **Install dependencies**:
   ```bash
   pip install pynput
Run in Standard Mode:

Bash
python main.py
Compile to Standalone EXE (Stealth):
To run GhostTrace on systems without Python installed:

Bash
pyinstaller --noconsole --onefile --name "WinSystemUpdate" main.py
🔒 Security & Ethics
This repository serves as a proof-of-concept for security auditing. By documenting how input monitors work, we can better understand how to defend against them and improve endpoint security.

Developed by Simone Ethan Alapens Aspiring Cybersecurity Researcher

