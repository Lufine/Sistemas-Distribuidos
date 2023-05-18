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
        message = input('Digite uma solicitação para enviar ao servidor (ou "sair" para encerrar): ')

        if message.lower() == 'sair':
            break

        # Envia a solicitação para o servidor
        request_message = 'REQ ' + message
        client_socket.send(request_message.encode())

        # Recebe a resposta do servidor
        response = client_socket.recv(1024).decode()

        print('Resposta recebida do servidor:', response)

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == '__main__':
    start_client()
