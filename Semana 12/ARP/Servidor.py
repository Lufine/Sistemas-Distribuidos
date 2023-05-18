import socket

def start_server():
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 12345  # Porta para conexão

    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o socket ao host e porta
    server_socket.bind((host, port))

    # Habilita o servidor para receber conexões
    server_socket.listen(1)

    print('Aguardando conexões...')

    # Aceita a primeira conexão recebida
    client_socket, addr = server_socket.accept()
    print('Conexão estabelecida com:', addr)

    while True:
        # Recebe a mensagem do cliente
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print('Mensagem recebida do cliente:', data)

        # Envia a mensagem de confirmação para o cliente
        confirmation_message = 'Confirmação: ' + data
        client_socket.send(confirmation_message.encode())

    # Fecha a conexão com o cliente
    client_socket.close()
    print('Conexão encerrada.')

if __name__ == '__main__':
    start_server()
