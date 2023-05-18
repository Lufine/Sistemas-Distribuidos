import socket

def start_client():
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 12345  # Porta para conexão

    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((host, port))

    while True:
        # Solicita ao usuário para digitar uma mensagem
        message = input('Digite uma mensagem para enviar ao servidor (ou "sair" para encerrar): ')

        if message.lower() == 'sair':
            break

        # Envia a mensagem para o servidor
        client_socket.send(message.encode())

        # Recebe a mensagem de confirmação do servidor
        confirmation_message = client_socket.recv(1024).decode()

        print('Mensagem de confirmação recebida do servidor:', confirmation_message)

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == '__main__':
    start_client()
