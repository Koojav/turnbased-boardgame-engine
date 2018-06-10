from tcp.config import Config
import socketserver
import time
import threading


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class GameTCPServer:

    def __init__(self, input_handler):
        self.input_handler = input_handler

        print("Starting TCP Server...")

        server = ThreadedTCPServer(Config.server_address, GameRequestHandler)
        with server:
            # Start a thread with the tcp -- that thread will then start one
            # more thread for each request
            server_thread = threading.Thread(target=server.serve_forever)
            # Exit the tcp thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            # server_thread.join()
            print("Server loop running in thread:", server_thread.name)

            # TODO: Figure out proper way
            time.sleep(3600)


class GameRequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our tcp.

    It is instantiated once per connection to the tcp, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        while True:

            data = str(self.request.recv(1024), 'ascii')
            cur_thread = threading.current_thread()
            response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
            # TODO: self.tcp - should be able to access self.tcp.game_controller
            if len(data) > 0:
                self.request.sendall(response)
                print(response)
            time.sleep(1)







