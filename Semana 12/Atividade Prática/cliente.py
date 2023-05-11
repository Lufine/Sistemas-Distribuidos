#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Aluno: Luiz Filipe Neuwirth
#Data: 11/05/2023

import socket

# define as informações do socket multicast
multicast_group = ('224.3.29.71', 16255)

# cria o socket multicast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia uma mensagem para o servidor
message = input('Digite a mensagem a sera invertida: ')
sock.sendto(message.encode('utf-8'), multicast_group)

# espera receber a mensagem invertida de volta do servidor
data, server = sock.recvfrom(1024)
print('Mensagem invertida:', data.decode('utf-8'))

#Este código cria um socket multicast UDP e envia uma mensagem para o servidor. Ele então espera receber a mensagem invertida de volta do servidor e imprime a mensagem na tela.
