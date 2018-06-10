import socket

client_name = "Roger"
message_count = 0

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to tcp and send data
    sock.connect(("localhost", 9999))

    while True:
        message = client_name + ": " + str(message_count)
        message_count += 1
        sock.sendall(bytes(message + "\n", "utf-8"))

        # Receive data from the tcp and shut down
        received = str(sock.recv(1024), "utf-8")

        print(client_name + " sent:     {}".format(message))
        print(client_name + " received: {}".format(received))

        # time.sleep(.1)


