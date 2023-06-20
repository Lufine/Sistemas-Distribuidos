import xmlrpc.server

class StringInverter:
    def invert_string(self, string):
        return string[::-1]

# Cria o servidor RPC
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(StringInverter())

print("Servidor de Inversão de String iniciado. Aguardando conexões...")

# Inicia o servidor
server.serve_forever()
