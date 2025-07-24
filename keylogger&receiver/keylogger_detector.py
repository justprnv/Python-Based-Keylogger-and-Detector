import tkinter as tk
from tkinter import messagebox, scrolledtext
import psutil
import winsound

# Modules commonly used in keyloggers
SUSPICIOUS_MODULES = [
    "pynput", "pyperclip", "keyboard", "mouse", "keylogger", "win32gui"
]

flagged_processes = []

class KeyloggerDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Detector - Manual Scan")
        self.root.geometry("750x500")

        self.log_area = scrolledtext.ScrolledText(root, state='disabled')
        self.log_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.scan_btn = tk.Button(root, text="🔍 Scan for Keyloggers", command=self.scan_now, width=25)
        self.scan_btn.pack(pady=10)

    def append_log(self, message):
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, message + '\n')
        self.log_area.see(tk.END)
        self.log_area.config(state='disabled')

    def scan_now(self):
        global flagged_processes
        flagged_processes.clear()
        self.append_log("[INFO] Scanning for suspicious keylogging behavior...")

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                name = proc.info['name']
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
                if 'python' not in name.lower():
                    continue

                # --- Deep memory scan for loaded modules ---
                suspicious_lib_found = False
                try:
                    for mmap in proc.memory_maps():
                        for lib in SUSPICIOUS_MODULES:
                            if lib.lower() in mmap.path.lower():
                                suspicious_lib_found = True
                                break
                        if suspicious_lib_found:
                            break
                except Exception:
                    continue  # Skip processes we can't access

                if suspicious_lib_found:
                    info = f"⚠️ PID: {proc.pid} | {name} | {cmdline}"
                    self.append_log(info)
                    flagged_processes.append(proc)
                    self.alert_user(info)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        if not flagged_processes:
            self.append_log("✅ No suspicious keylogging activity detected.")

    def alert_user(self, message):
        winsound.Beep(1000, 300)
        messagebox.showwarning("Suspicious Process Detected", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerDetectorApp(root)
    root.mainloop()
