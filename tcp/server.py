import socketserver
import threading
import queue
import time


class GameTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, server_address, request_handler_class, bind_and_activate=True):
        super().__init__(server_address, request_handler_class, bind_and_activate)

        # Thread synchronized queue of orders from all instances of GameTCPRequestHandler
        self.orders_from_clients = queue.Queue()

        # This will be None until all clients supply first round of orders, thus registering them and starting the game
        self._board_state = None

    @property
    def board_state(self):
        return self._board_state

    @board_state.setter
    def board_state(self, value):
        self._board_state = value

    def retrieve_orders(self):
        """
        Retrieves all stored orders from this round and resets their queue so they won't be left over for the next round
        :return: Orders from clients for current round
        """
        orders = self.orders_from_clients
        self.orders_from_clients = queue.Queue()
        return orders


class GameTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our tcp.

    It is instantiated once per connection to the tcp, and must
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, request, client_address, server):
        # Used to indicate which board state was already propagated to the client connected via this instance of
        # GameTCPRequestHandler
        self.last_sent_board_id = -1

        super().__init__(request, client_address, server)

    def handle(self):

        server = self.server

        while True:
            client_order = str(self.request.recv(1024), 'ascii')

            # TODO: Improve recognition of point when all data, in one order, has been fully received
            if len(client_order) > 0:
                server.orders_from_clients.put(client_order)
                print("Orders in queue: " + str(server.orders_from_clients.qsize()))

            self.wait_for_new_board_state()

            response_board_state = bytes("Sending board_state[{}]: {}".format(server.board_state.id, server.board_state.state), 'ascii')
            self.request.sendall(response_board_state)
            self.last_sent_board_id = server.board_state.id
            print(response_board_state)

    def wait_for_new_board_state(self):
        while self.server.board_state is None or self.server.board_state.id <= self.last_sent_board_id:
            time.sleep(1)
