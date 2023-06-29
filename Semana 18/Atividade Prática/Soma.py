import Pyro4

uri = input("Digite a URI do servidor: ")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

server = Pyro4.Proxy(uri)
result = server.add_numbers(a, b)

print("Resultado da soma:", result)
