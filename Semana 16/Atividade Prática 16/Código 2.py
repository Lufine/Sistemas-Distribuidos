import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = cliente.somar(num1, num2)
print("Resultado da soma: ", resultado)