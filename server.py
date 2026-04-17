import socket


def start_server():
    host = input("Введите IP клиента: ")
    port = 4444

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print("Соединение с клиентом установлено")

        filename = input("Введите путь к файлу для удаления: ")
        client.send(f"DELETE:{filename}".encode())

        response = client.recv(1024).decode()
        print(f"Ответ клиента: {response}")

        client.close()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    start_server()