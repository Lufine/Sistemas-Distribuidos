import Pyro4

@Pyro4.expose
class NumberAdder(object):
    def add_numbers(self, a, b):
        return a + b

daemon = Pyro4.Daemon()
uri = daemon.register(NumberAdder)

print("URI do servidor:", uri)
print("Servidor RMI iniciado. Aguardando solicitações...")

daemon.requestLoop()
