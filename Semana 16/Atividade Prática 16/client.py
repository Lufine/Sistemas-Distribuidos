import xmlrpc.client

# Cria uma conexão com o servidor RPC
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Solicita ao usuário para digitar dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Chama o procedimento remoto do servidor para somar os números
resultado = client.soma_numeros(num1, num2)

# Exibe o resultado da soma
print("Resultado da soma:", resultado)
