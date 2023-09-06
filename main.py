import socket
import threading
import time

# Constants
RECEIVE_SERVER_IP = '10.17.7.218'  # Replace with the actual server IP address
RECEIVE_SERVER_PORT = 9801  # Replace with the actual server port

SEND_SERVER_IP = 'localhost'  # Replace with the actual IP address of the send server
SEND_SERVER_PORT = 3000  # Replace with the actual port of the send server

TARGET_LINES = 1000
# Data storage to store unique lines
unique_lines = set()


def receive_data():
    receive_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        try:
            receive_client_socket.connect((RECEIVE_SERVER_IP, RECEIVE_SERVER_PORT))
            break  # If connection succeeds, exit the loop
        except socket.error as e:
            print(f"[{RECEIVE_SERVER_IP}]Error connecting to the receive server: {e}")
            # You can add further error handling here, such as retries or exiting the program

    while len(unique_lines) < TARGET_LINES:
        # Send the request to the server
        receive_client_socket.send("SENDLINE\n".encode())

        # Receive the response from the server
        response = receive_client_socket.recv(1024).decode()

        # Split the response into lines and process them
        lines = response.split('\n')

        if lines[0] != "-1":
            unique_lines.add(response)

    receive_client_socket.close()

# Function to continuously send "SENDLINE\n" request to the send server
def send_data():
    send_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        try:
            send_client_socket.connect((SEND_SERVER_IP, SEND_SERVER_PORT))
            break  # If connection succeeds, exit the loop
        except socket.error as e:
            print(f"[{SEND_SERVER_IP}]Error connecting to the send server: {e}")
            # You can add further error handling here, such as retries or exiting the program

    while len(unique_lines) < TARGET_LINES:
        data_to_send = '\n'.join(unique_lines)
        send_client_socket.send(data_to_send.encode())

        # Introduce a 1-second delay
        time.sleep(1)


    send_client_socket.close()


if __name__ == '__main__':
    # Create threads for receiving and sending data
    receive_thread = threading.Thread(target=receive_data)
    send_thread = threading.Thread(target=send_data)

    # Start both threads
    receive_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

    print("Received 1000 unique lines from the send server.")