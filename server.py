import socket

host = 'localhost'  # Define the host as localhost
port = 2458  # Define the port number as 2458


def start_server():
    # Create a socket object for the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))  # Bind the socket to the host and port
        server_socket.listen(1)  # Listen for incoming connections
        print('Server is listening for connections...')

        connection_socket, address = server_socket.accept() # Accept a connection
        print('Connected by', address)

        while True:
            recieved_message = connection_socket.recv(2048).decode() # Receive a message from the client
            if not recieved_message:  # If the message is empty, break the loop
                break
            print("Client message: ", recieved_message)

            if recieved_message.strip().lower() == "hello":  # If the message is "hello"
                response = "Hello, What's your name?"
                connection_socket.send(response.encode())  # Send a response to the client

                name = connection_socket.recv(1024).decode()  # Receive a name from the client
                print("Name of the Client: ", name)

                welcome_message = f"Hello {name}, Welcome to SIT202"
                connection_socket.send(welcome_message.encode()) # Send a welcome message to the client
            else:
                error_message = "Error!! Message not sent"
                connection_socket.send(error_message.encode())   # Send an error message to the client

        connection_socket.close()  # Close the connection
        server_socket.close()  # Close the server socket


if __name__ == '__main__':
    start_server()  # Call the start_server() function
