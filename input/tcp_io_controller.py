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
        self.server = GameTCPServer(Config.server_address, GameTCPRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True

    def start(self):
        print("Starting TCP server...")
        # Start a thread with the tcp -- that thread will then start one more thread for each request
        self.server_thread.start()

    def propagate_board_state(self, board_state: BoardState):
        # It's enough to set new value to server.board_state and it will take care of propagating it further
        # based on last sent and current BoardState.id
        self.server.board_state = board_state

    def wait_for_all_orders(self):
        while self.server.orders_from_clients.qsize() < self.player_count:
            # print("Waiting for orders: {}/{}".format(self.server.orders_from_clients.qsize(), self.player_count))
            time.sleep(1)

        print("Waiting for all orders: Complete.")
        return self.server.retrieve_orders()
