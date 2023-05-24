import socket
from select import select

# асинхронность при помощи event_loop
# domain:port
to_monitor = []

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('localhost', 5000))
socket_server.listen()


def accept_connection(socket_server):
    client_socket, addr = socket_server.accept()
    print('Connect from', addr)

    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4090)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:   
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], []) # read, write, errors
        
        for sock in ready_to_read:
            if sock is socket_server:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(socket_server)
    event_loop()
    # accept_connection(socket_server)