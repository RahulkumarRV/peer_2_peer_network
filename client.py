import socket

# Constants
HOST = '127.0.0.1'
PORT = 3000

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    # Send a message to the server
    message = input("Enter a message to send to the server (or 'exit' to quit): ")
    client.send(message.encode())

    if message.lower() == 'exit':
        break

    # Receive and print the server's response
    response = client.recv(1024).decode()
    print(f"Received from server: {response}")

# Close the client socket
client.close()
