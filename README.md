# Client-Server Remote Control Demo (Python)

## Description
This project demonstrates a simple client-server architecture in Python using sockets. It simulates remote command execution and basic interaction between two hosts.

The project includes both direct connection and reverse connection modes, as well as a simple persistence mechanism for educational purposes.

 This project is created for educational purposes only.

---

## Features
- Client-server communication via TCP sockets
- Command execution (file deletion simulation)
- Reverse connection (client connects back to server)
- Basic persistence mechanism (Linux autostart)
- Daemon mode for background execution

---

## Project Structure
- `client.py` – basic listener client
- `clientmod.py` – extended client with persistence and reverse connection
- `server.py` – simple client connector
- `servermod.py` – reverse connection server

---

## How to Run

### Listener mode
1. Run client:
```bash
python3 client.py
