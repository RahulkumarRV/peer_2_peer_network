import socket

# Constants
SERVER_IP = '10.17.7.218'  # Replace with the actual server IP address
SERVER_PORT = 9801  # Replace with the actual server port
TARGET_LINES = 1000

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Data storage to store unique lines
unique_lines = set()

# Keep sending requests until we collect 1000 unique lines
while len(unique_lines) < TARGET_LINES:
    # Send the request to the server
    client_socket.send("SENDLINE\n".encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode()

    # Split the response into lines and process them
    lines = response.split('\n')
    
    if lines[0] != "-1":
        unique_lines.add(response)

# Close the client socket
client_socket.close()

# Print the collected unique lines
print("Collected Unique Lines:")
for line in unique_lines:
    print(line)
