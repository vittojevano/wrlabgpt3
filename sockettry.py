import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.11.76', 10000)
message = '私の名前はパルロです'  # This is the message to be sent, encoded in UTF-8

# Encode the message in UTF-8 and send it to the server
sock.sendto(message.encode('utf-8'), server_address)

# Close the socket
sock.close()
