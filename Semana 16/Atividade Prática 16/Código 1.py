import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")
mensagem = input("Digite uma mensagem para ser invertida: ")
resultado = cliente.inverter(mensagem)
print("Resultado da inversão: ", resultado)