#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Aluno: Luiz Filipe Neuwirth
#Data: 11/05/2023

import socket
import struct

# define as informações do socket multicast
multicast_group = '224.3.29.71'
server_address = ('', 16255)

# cria o socket multicast e o associa ao endereço do servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

# adiciona o socket ao grupo multicast
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    # espera receber dados do cliente
    print('\nEsperando receber mensagem...')
    data, address = sock.recvfrom(1024)
    print('Recebido {} bytes de {}.'.format(len(data), address))

    # inverte a string recebida
    message = data.decode('utf-8')
    inverted_message = message[::-1]

    # envia a string invertida de volta para o cliente
    print('Enviando mensagem invertida de volta para', address)
    sock.sendto(inverted_message.encode('utf-8'), address)

#Este código cria um socket multicast UDP e o associa a um endereço e porta específicos. 
 
#Em seguida, ele adiciona o socket ao grupo multicast especificado e entra em um loop para esperar receber dados do cliente. Quando uma mensagem é recebida, o código inverte a string e envia a string invertida de volta para o cliente.

#Para testar este código, necessita da exceução em um terminal e, em seguida, executar o seguinte código em outro terminal para enviar uma mensagem ao servidor: