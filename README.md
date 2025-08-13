# Python-Based Keylogger and Detector

A comprehensive Python project that demonstrates both keylogging capabilities and detection mechanisms. This project includes a keylogger with remote monitoring capabilities and a detector application to identify suspicious keylogging behavior.

## ⚠️ **IMPORTANT SECURITY DISCLAIMER**

**This project is for EDUCATIONAL and RESEARCH purposes ONLY.**
- Do NOT use this software to monitor others without explicit consent
- Do NOT deploy in production environments
- Do NOT use for malicious purposes
- Always comply with local laws and regulations
- Use only on systems you own or have explicit permission to test

## 🏗️ Project Structure

```
Python-Based-Keylogger-and-Detector-main/
├── keylogger&receiver/
│   ├── keylogger_sender.py      # Keylogger client application
│   ├── keylogger_detector.py    # Keylogger detection tool
│   ├── # receiver_gui.py        # Remote monitoring receiver
│   └── keylog_output.txt        # Local log file (generated)
└── README.md
```

## 🚀 Features

### Keylogger Sender (`keylogger_sender.py`)
- **Real-time keystroke logging** with timestamps
- **Mouse click monitoring** with coordinates
- **Active window tracking** across different applications
- **Clipboard monitoring** for copied content
- **Remote data transmission** via TCP socket
- **Self-destruct capability** with remote kill command
- **Cross-platform support** (Windows, macOS, Linux)
- **Console hiding** capability (Windows)

### Keylogger Detector (`keylogger_detector.py`)
- **Process scanning** for suspicious Python processes
- **Memory mapping analysis** to detect keylogging libraries
- **Real-time alerts** with audio notifications
- **GUI interface** for easy monitoring
- **Suspicious module detection** including:
  - `pynput` (keyboard/mouse input)
  - `pyperclip` (clipboard access)
  - `keyboard` (keyboard events)
  - `mouse` (mouse events)
  - `win32gui` (Windows GUI access)

### Remote Receiver (`# receiver_gui.py`)
- **Real-time data reception** from keylogger clients
- **Live monitoring interface** with scrollable text area
- **Remote kill command** to terminate keylogger
- **Connection status** monitoring
- **Network-based communication**

## 📋 Prerequisites

- Python 3.7 or higher
- Windows, macOS, or Linux operating system
- Network access for remote monitoring features

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Python-Based-Keylogger-and-Detector-main
   ```

2. **Install required dependencies:**
   ```bash
   pip install pynput pyperclip psutil pywin32
   ```

   **Note:** `pywin32` is only required on Windows systems.

3. **Configure network settings:**
   - Edit `keylogger_sender.py` and update `REMOTE_IP` with your receiver's IP address
   - Ensure firewall allows connections on port 65432

## 🎯 Usage

### 1. Starting the Keylogger Detector
```bash
cd keylogger&receiver
python keylogger_detector.py
```
- Click "🔍 Scan for Keyloggers" to perform manual scans
- Monitor the log area for suspicious processes
- Audio alerts will notify you of detected threats

### 2. Starting the Remote Receiver
```bash
cd keylogger&receiver
python "# receiver_gui.py"
```
- The receiver will start listening on port 65432
- Wait for keylogger client connections
- Monitor incoming data in real-time
- Use "☠ Send Kill Signal" to terminate connected keyloggers

### 3. Running the Keylogger (Educational Use Only)
```bash
cd keylogger&receiver
python keylogger_sender.py
```
- Press ESC to stop the keylogger
- Data is logged locally to `keylog_output.txt`
- Remote data transmission requires receiver to be running

## 🔍 Detection Capabilities

The detector identifies suspicious processes by:
- **Library Analysis:** Scanning for known keylogging libraries in memory
- **Process Monitoring:** Tracking Python processes with suspicious behavior
- **Real-time Scanning:** Continuous monitoring with manual scan triggers
- **Alert System:** Audio and visual notifications for threats

## 🌐 Network Configuration

### Default Settings
- **Port:** 65432
- **Protocol:** TCP
- **Bind Address:** 0.0.0.0 (all interfaces)

### Customization
Edit these variables in the respective files:
```python
# In keylogger_sender.py
REMOTE_IP = "192.168.0.17"  # Receiver's IP address
REMOTE_PORT = 65432          # Communication port

# In # receiver_gui.py
HOST = "0.0.0.0"            # Listening interface
PORT = 65432                 # Listening port
```

## 🛡️ Security Features

- **Self-destruct mechanism** with remote kill command
- **Process hiding** capabilities
- **Encrypted communication** (can be implemented)
- **Log file cleanup** on termination
- **Cross-platform compatibility**

## 📱 Platform Support

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| Keystroke Logging | ✅ | ✅ | ✅ |
| Mouse Monitoring | ✅ | ✅ | ✅ |
| Window Tracking | ✅ | ✅ | ⚠️ |
| Clipboard Access | ✅ | ✅ | ✅ |
| Console Hiding | ✅ | ❌ | ❌ |
| Process Detection | ✅ | ✅ | ✅ |

## 🚨 Troubleshooting

### Common Issues

1. **Import Errors:**
   - Ensure all dependencies are installed
   - Use virtual environment for clean dependency management

2. **Permission Denied:**
   - Run with administrator privileges (Windows)
   - Check file permissions on Unix systems

3. **Connection Issues:**
   - Verify IP address and port configuration
   - Check firewall settings
   - Ensure receiver is running before sender

4. **Detection False Positives:**
   - Whitelist legitimate applications
   - Adjust suspicious module list as needed

## 📚 Educational Value

This project demonstrates:
- **Input monitoring** techniques
- **Process detection** methodologies
- **Network communication** protocols
- **Cross-platform development** strategies
- **Security tool development** principles

## 🔒 Legal and Ethical Considerations

- **Educational Use Only:** This software is designed for learning and research
- **Consent Required:** Only use on systems you own or have explicit permission to test
- **Legal Compliance:** Ensure compliance with local laws and regulations
- **Responsible Disclosure:** Report security vulnerabilities responsibly

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows Python PEP 8 standards
- Security best practices are maintained
- Documentation is updated accordingly
- Tests are included for new features

## 📄 License

This project is provided as-is for educational purposes. Users are responsible for ensuring compliance with applicable laws and regulations.

## ⚡ Performance Notes

- **Memory Usage:** Minimal impact on system resources
- **CPU Usage:** Low overhead during normal operation
- **Network:** Minimal bandwidth usage for remote monitoring
- **Storage:** Log files grow based on activity level

## 🔮 Future Enhancements

- [ ] Encrypted communication channels
- [ ] Machine learning-based threat detection
- [ ] Web-based monitoring interface
- [ ] Mobile app support
- [ ] Advanced evasion techniques
- [ ] Integration with security frameworks

---

**Remember: With great power comes great responsibility. Use this knowledge ethically and legally.**
