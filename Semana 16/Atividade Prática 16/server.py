from xmlrpc.server import SimpleXMLRPCServer

def inverter_string(texto):
    return texto[::-1]

def somar_numeros(a, b):
    return a + b

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(inverter_string, "inverter_string")
server.register_function(somar_numeros, "somar_numeros")
print("Servidor RPC iniciado. Aguardando solicitações...")

server.serve_forever()
