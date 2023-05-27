import socket
import select

# Aсинхронность на генераторах 
# domain:port

tasks = []

to_read = {}
to_write = {}


def server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost', 5000))
    socket_server.listen()

    while True:

        yield ('read', socket_server)
        client_socket, addr = socket_server.accept() # read

        print('Connect from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:

        yield ('read', client_socket)
        request = client_socket.recv(4090) # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response) # write
    
    client_socket.close()


def event_loop():
    
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ =  select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))


        try:
            task = tasks.pop(0)

            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')

tasks.append(server())
event_loop()