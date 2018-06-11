import threading
import time
from .base_io_controller import BaseIOController
from tcp.server import GameTCPServer
from tcp.server import GameTCPRequestHandler
from logic.board_state import BoardState


class Config:
    host = "localhost"
    port = 9999
    server_address = (host, port)


class TCPIOController(BaseIOController):
    def __init__(self, player_count: int):
        super().__init__(player_count)

        print("Starting TCP server...")
        self.server = GameTCPServer(Config.server_address, GameTCPRequestHandler)
        with self.server:
            # Start a thread with the tcp -- that thread will then start one more thread for each request
            server_thread = threading.Thread(target=self.server.serve_forever)
            # Exit the tcp thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            print("Server started successfully.")
            server_thread.join()

    def propagate_board_state(self, board_state: BoardState):
        # It's enough to set new value to server.board_state and it will take care of propagating it further
        # based on last sent and current BoardState.id
        self.server.board_state = board_state

        return self.wait_for_all_orders()

    def wait_for_all_orders(self):
        while self.server.orders_from_clients.qsize() < self.player_count:
            print("Waiting for orders: {}/{}".format(self.server.orders_from_clients.qsize(), self.player_count))
            time.sleep(.1)

        print("Waiting for all orders: Complete.")
        return self.server.retrieve_orders()
