import time
from .base_input_controller import BaseInputController
from tcp.server import GameTCPServer


class TCPInputController(BaseInputController):
    def __init__(self, player_count: int):
        super().__init__(player_count)
        self.game_server = GameTCPServer(self.handle_client_input)
        self.orders = []

    def request_orders_from_all_players(self, map_state):
        while len(self.orders) < self.player_count:
            time.sleep(2)
        return []
    
    def handle_client_input(self, data):
        pass

