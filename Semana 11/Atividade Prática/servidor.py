# Curso de Engenharia de Software - UniEVANGÉLICA
# Disciplina de Sistemas Distribuidos
# Aluno: Luiz Filipe Neuwirth
# Data: 11/05/2023

import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000         # Porta de comunicação

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escutando em {HOST}:{PORT}")

while True:
    # Aguarda uma conexão
    client_socket, address = server_socket.accept()

    # Recebe a mensagem enviada pelo cliente
    message = client_socket.recv(1024).decode()

    # Exibe a mensagem no console do servidor
    print(f"Mensagem recebida do cliente {address}: {message}")

    # Encerra a conexão com o cliente
    client_socket.close()
