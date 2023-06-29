import Pyro4

@Pyro4.expose
class Saludo:
    def saludar(self):
        return  'Hola'


daemon = Pyro4.Daemon()

uri = daemon.register(Saludo)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()