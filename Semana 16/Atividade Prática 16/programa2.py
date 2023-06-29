import xmlrpc.client

# Conectar ao servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Ler os números do usuário
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

# Chamar o método remoto no servidor para somar os números
resultado = server.somar_numeros(a, b)

# Exibir o resultado
print("Resultado da soma:", resultado)
