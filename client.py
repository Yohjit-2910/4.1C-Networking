# Documentation
# Name : Yohjit Chopra
# Roll No. 2110994798

import socket

# Set the host and port number
host = 'localhost'
port = 2458

# Create a client socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server using the host and port number
client.connect((host, port))

# Send a message to the server
full_message = "Hello"
client.send(full_message.encode())
print("Message sent: ", full_message)

# Receive the response from the server
response = client.recv(2048).decode()
print("Server response is: ", response)

# Check if the response is asking for the client's name
if "What's your name?" in response:
    # Ask the client to input their name
    name = input("Enter your name: ")
    client.send(name.encode())
    print("Sent name to server: ", name)

    # Receive the welcome message from the server
    welcome_message = client.recv(2048).decode()
    print("Server response: ", welcome_message)
else:
    # Print an error message if the server's response is not expected
    print("Error: ", response)

# Close the client socket
client.close()
