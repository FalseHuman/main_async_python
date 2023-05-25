import socket
import selectors

# асинхронность при помощи event_loop - callbacks
# domain:port

selector = selectors.DefaultSelector()


def server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost', 5000))
    socket_server.listen()

    selector.register(fileobj=socket_server, 
                      events=selectors.EVENT_READ,
                      data=accept_connection)


def accept_connection(socket_server):
    client_socket, addr = socket_server.accept()
    print('Connect from', addr)
    selector.register(fileobj=client_socket, 
                      events=selectors.EVENT_READ,
                      data=send_message)

    


def send_message(client_socket):
    request = client_socket.recv(4090)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else: 
        selector.unregister(client_socket) 
        client_socket.close()


def event_loop():
    while True:
        events = selector.select() # (key, events)

        # Selectorkey
        # fileobj
        # events
        # data 

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
    # accept_connection(socket_server)