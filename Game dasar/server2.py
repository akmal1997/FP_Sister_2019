import Pyro4
from tictactoedasar import *

#current server
# Jangan lupa pyro4-ns -n localhost -p 7777
def run_server(hostname):
    daemon = Pyro4.Daemon(host="localhost")
    name_server = Pyro4.locateNS("localhost", 7777)
    exposed_master_server = Pyro4.expose(ttt)
    uri_host_server = daemon.register(exposed_master_server)
    print("URI host server : ", uri_host_server)
    name_server.register(hostname, uri_host_server)
    daemon.requestLoop()


if __name__ == '__main__':
    input_host_name = "hostname"
    run_server(input_host_name.strip())
