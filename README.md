# VLUB-X
This a Vlub lab made by me for my virtual lab

# 💀 VLUB-X: Vulnerable Linux Utility Box – eXploit Edition

VLUB-X is a lightweight, portable, and intentionally vulnerable web server built with Python Flask and designed for ethical hacking practice, CTF prep, and cybersecurity education.

Host it on a Raspberry Pi Zero 2W or any Linux system and use it as your personal hackable target!

---

## 🚀 Features

- 🔓 **XSS Lab** – reflected XSS attack practice (`/hello`)
- 💉 **SQLi Simulation** – vulnerable login simulation (`/login`)
- 🖥️ **Command Injection** – ping a host via shell (`/ping`)
- 🌐 **SSRF Playground** – fetch internal/external URLs (`/ssrf`)
- 🔐 **Broken Access Control** – open admin panel (`/admin`)
- 💣 **Web Defacement Tool** – POST HTML to overwrite a page (`/deface`)
- 🎭 **Live Defaced Page** – simulate the aftermath (`/hacked`)
- 🧠 **Hacking Console UI** – animated fake terminal (`/`)

---

## 🧱 Project Structure

vlub-x/
├── app.py # Main Flask app
├── templates/ # (Optional if using deface route)
└── static/ # (Optional for future CSS/JS assets)

yaml
Copy
Edit

---

## 🛠️ Getting Started

### Requirements

- Python 3.x
- Flask (`pip install flask`)
- requests module (`pip install requests`)

### Run the Server

```bash
python3 app.py
