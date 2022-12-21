import socket
import sys


def initSocket(ip, port):
    # Set up a TCP/IP server
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to server address and port 81
    server_address = (ip, port)
    tcp_socket.bind(server_address)

    # Listen on port
    tcp_socket.listen(1)

    while True:
        # print("Waiting for connection")

        connection, client = tcp_socket.accept()
        print(client)

        try:
            print("Connected to client IP: {}".format(client))

            while True:
                data = connection.recv(32)
                print("Received data: {}".format(data))
                tcp_socket.send('json_config/config_sala1')

                if not data:
                    break

        finally:
            connection.close()
