import xmlrpc.client

# Conectar ao servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Ler a string do usuário
texto = input("Digite a mensagem a ser invertida: ")

# Chamar o método remoto no servidor para inverter a string
resultado = server.inverter_string(texto)

# Exibir o resultado
print("String invertida:", resultado)
