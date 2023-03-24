import socket


class UDPClient(object):

    def SendUDP(self, input_message=None):
        server_address = ('192.168.11.76', 10000)
        # client_ip = "192.168.11.75"
        # client_port = 5005
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # sock.bind((client_ip, client_port))
        msg = input_message
        sock.sendto(msg.encode('utf-8'), server_address)

        # print(data)
        sock.close()

    def ReceiveTCP(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("192.168.11.1", 30000))
        server_socket.listen()

        client_socket, client_address = server_socket.accept()
        message = client_socket.recv(1024).decode("utf-8")
        print(message)

        client_socket.close()
        server_socket.close()
