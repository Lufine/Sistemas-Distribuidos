# Curso de Engenharia de Software - UniEVANGÉLICA
# Disciplina de Sistemas Distribuidos
# Aluno: Luiz Filipe Neuwirth
# Data: 11/05/2023

import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000         # Porta de comunicação

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))

# Envia uma mensagem para o servidor
message = input("Digite uma mensagem: ")
client_socket.send(message.encode())

# Encerra a conexão com o servidor
client_socket.close()
