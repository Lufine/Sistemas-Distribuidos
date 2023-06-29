import Pyro4

@Pyro4.expose
class StringInverter(object):
    def invert_string(self, text):
        return text[::-1]

daemon = Pyro4.Daemon()
uri = daemon.register(StringInverter)

print("URI do servidor:", uri)
print("Servidor RMI iniciado. Aguardando solicitações...")

daemon.requestLoop()
