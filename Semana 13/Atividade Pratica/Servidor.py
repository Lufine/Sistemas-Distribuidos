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

        print('Solicitação recebida do cliente:', data)

        # Processa a solicitação do cliente
        response_data = process_request(data)

        # Envia a resposta para o cliente
        response_message = 'RESP ' + response_data
        client_socket.send(response_message.encode())

    # Fecha a conexão com o cliente
    client_socket.close()
    print('Conexão encerrada.')

def process_request(request):
    # Lógica para processar a solicitação do cliente
    # e retornar a resposta adequada
    # Aqui você implementaria a lógica específica
    # do seu projeto integrador
    response = 'Resposta do servidor'
    return response

if __name__ == '__main__':
    start_server()
