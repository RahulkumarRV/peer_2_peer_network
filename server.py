import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 3000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max queue length is 5)
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

def handle_client(client_socket):
    # Code to handle client communication goes here
    data = client_socket.recv(1024).decode()
    lines = data.split('\n')

    for line in lines:
        print(line)
    client_socket.close()

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Handle client communication here
    # For example, you can send/receive data with client_socket

    # Close the client socket when done
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

