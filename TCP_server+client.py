import socket
import threading
import sys


def start_server():
    server_address = ('localhost', 12345)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    clients = {}
    nicknames = {}

    def handle_client(client_socket):
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                if message.startswith('/nick'):
                    _, nickname = message.split(' ', 1)
                    nicknames[client_socket] = nickname.strip()
                    broadcast(f'Сервер: {nickname} присоединился к чату!', client_socket)
                elif message.lower().strip() == '/exit':
                    client_socket.send('/exit'.encode('utf-8'))
                    break
                else:
                    nickname = nicknames.get(client_socket, "Неизвестный")
                    broadcast(f'{nickname}: {message}', client_socket)
        except:
            pass
        finally:
            clients.pop(client_socket, None)
            nickname = nicknames.pop(client_socket, "Неизвестный")
            broadcast(f'Сервер: {nickname} покинул чат.', client_socket)
            client_socket.close()

    def broadcast(message, sender_socket=None):
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()

    print('Сервер запущен и ожидает подключений...')
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Подключен клиент: {client_address}')
        clients[client_socket] = client_address
        threading.Thread(target=handle_client, args=(client_socket,)).start()


def start_client():
    server = 'localhost'
    port = 12345
    nickname = input("Введите ваш ник: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server, port))
    client_socket.send(f'/nick {nickname}'.encode('utf-8'))

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message == '/exit':
                    print("Вы отключены от сервера.")
                    break
                print(message)
            except:
                print("Отключение от сервера...")
                client_socket.close()
                break

    threading.Thread(target=receive_messages).start()
    try:
        while True:
            message = input()
            if message.lower().strip() == '/exit':
                client_socket.send('/exit'.encode('utf-8'))
                break
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        client_socket.send('/exit'.encode('utf-8'))
    finally:
        client_socket.close()


if len(sys.argv) > 1:
    if sys.argv[1] == '--server':
        start_server()
    elif sys.argv[1] == '--client':
        start_client()
    else:
        print("Используйте: --server для запуска сервера или --client для запуска клиента")
else:
    print("Укажите --server или --client в аргументах командной строки")
