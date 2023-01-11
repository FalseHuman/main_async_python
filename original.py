import socket

# domain:port

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('localhost', 5000))
socket_server.listen()

while True:
    print('Before .accept()')
    client_socket, addr = socket_server.accept()
    print('Connect from', addr)

    while True:
        print('Before .recv()')
        request = client_socket.recv(4090)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
    
    print('Outside inner while loop')
    client_socket.close()