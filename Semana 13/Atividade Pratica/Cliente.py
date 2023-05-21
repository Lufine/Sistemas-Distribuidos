#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Aluno: Luiz Filipe Neuwirth
#DATA: 21/05/2023 

import socket
import sqlite3

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Definir o protocolo de comunicação
# O protocolo consiste em mensagens no formato "tipo|dados"
# O tipo pode ser "MSG" para mensagens de texto ou "ITEM" para informações de item
# Os dados podem ser uma mensagem de texto ou informações de item no formato "nome|quantidade"
def receive_message(conn):
    data = conn.recv(1024).decode()
    parts = data.split('|')
    return parts[0], parts[1]

def send_message(conn, message):
    data = f"MSG|{message}".encode()
    conn.sendall(data)

def add_item_to_database(conn, item_name, item_quantity):
    # Conectar ao banco de dados
    conn = sqlite3.connect('nadespensa.db')
    c = conn.cursor()
    # Inserir o item na tabela de itens
    c.execute("INSERT INTO itens (nome, quantidade) VALUES (?, ?)", (item_name, item_quantity))
    conn.commit()
    conn.close()

def remove_item_from_database(conn, item_name):
    # Conectar ao banco de dados
    conn = sqlite3.connect('nadespensa.db')
    c = conn.cursor()
    # Remover o item da tabela de itens
    c.execute("DELETE FROM itens WHERE nome = ?", (item_name,))
    conn.commit()
    conn.close()

def update_item_in_database(conn, item_name, item_quantity):
    # Conectar ao banco de dados
    conn = sqlite3.connect('nadespensa.db')
    c = conn.cursor()
    # Atualizar a quantidade do item na tabela de itens
    c.execute("UPDATE itens SET quantidade = ? WHERE nome = ?", (item_quantity, item_name))
    conn.commit()
    conn.close()

def get_item_from_database(conn, item_name):
    # Conectar ao banco de dados
    conn = sqlite3.connect('nadespensa.db')
    c = conn.cursor()
    # Buscar o item na tabela de itens
    c.execute("SELECT * FROM itens WHERE nome = ?", (item_name,))
    item = c.fetchone()
    conn.close()
    return item

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Servidor aguardando conexões...')
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            # Receber a mensagem do cliente
            type, data = receive_message(conn)
            if type == 'MSG':
                print(f'Mensagem recebida: {data}')
                # Enviar uma mensagem de resposta
                send_message(conn, f'Recebido: {data}')
            elif type == 'ADD':
                print(f'Informações de item recebidas: {data}')
                # Adicionar o item ao banco de dados
                item_name, item_quantity = data.split('|')
                add_item_to_database(conn, item_name, item_quantity)
                # Enviar uma mensagem de resposta
                send_message(conn, f'Item adicionado: {item_name} ({item_quantity})')
            elif type == 'REMOVE':
                print(f'Informações de item recebidas: {data}')
                # Remover o item do banco de dados
                item_name = data
                remove_item_from_database(conn, item_name)
                # Enviar uma mensagem de resposta
                send_message(conn, f'Item removido: {item_name}')
            elif type == 'UPDATE':
                print(f'Informações de item recebidas: {data}')
                # Atualizar a quantidade do item no banco de dados
                item_name, item_quantity = data.split('|')
                update_item_in_database(conn, item_name, item_quantity)
                # Enviar uma mensagem de resposta
                send_message(conn, f'Item atualizado: {item_name} ({item_quantity})')
            elif type == 'GET':
                print(f'Solicitação de informações de item recebida: {data}')
                # Buscar o item no banco de dados
                item_name = data
                item = get_item_from_database(conn, item_name)
                if item:
                    # Enviar uma mensagem de resposta com as informações do item
                    send_message(conn, f'Item encontrado: {item[0]} ({item[1]})')
                else:
                    # Enviar uma mensagem de resposta informando que o item não foi encontrado
                    send_message(conn, f'Item não encontrado: {item_name}')
            else:
                print(f'Tipo de mensagem inválido: {type}')
                # Enviar uma mensagem de erro
                send_message(conn, f'Erro: tipo de mensagem inválido')