import socket
import threading

nickname = ""

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message.startswith(f"{nickname}:"):
                print(message)
        except:
            print("Você foi desconectado do servidor.")
            break

def main():
    global nickname
    nickname = input("Escolha seu apelido: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input()
        print(f"você: {message}")
        client.send(f"{nickname}: {message}".encode())

if __name__ == "__main__":
    main()
