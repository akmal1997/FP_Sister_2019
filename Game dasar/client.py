import Pyro4

#client
def get_fileserver_object(instance_name):
    uri = "PYRONAME:{}@127.0.0.1:7777" . format(instance_name)
    fserver = Pyro4.Proxy(uri)
    return fserver


if __name__ == '__main__':
    connection = get_fileserver_object("hostname")
    print(connection.hello())
