import Pyro4

uri = input("Digite a URI do servidor: ")
string_to_invert = input("Digite a string a ser invertida: ")

server = Pyro4.Proxy(uri)
result = server.invert_string(string_to_invert)

print("Resultado da inversão:", result)
