import socket
import os

HOST = '0.0.0.0'
PORT = 4444

def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return f"File {filename} deleted successfully"
        else:
            return f"File {filename} not found"
    except Exception as e:
        return f"Error: {e}"


def start_client():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Клиент запущен и ждёт подключения на порту {PORT}")

    while True:
        conn, addr = server.accept()
        print(f"Подключение от {addr}")
        data = conn.recv(1024).decode().strip()

        if data.startswith("DELETE:"):
            filename = data[7:]
            result = delete_file(filename)
            conn.send(result.encode())
        else:
            conn.send(b"Unknown command")
        conn.close()


if __name__ == "__main__":
    start_client()