from input.base_input_controller import BaseInputController
from .board_controller import BoardController


class GameController:

    def __init__(self, input_controller: BaseInputController):
        self.input_controller = input_controller
        self.board_controller = BoardController()

        # Game's main loop
        self.main_loop()

    def execute_orders(self):
        pass

    def broadcast_map_state(self):
        pass

    def main_loop(self):
        while True:
            orders = self.input_controller.request_orders_from_all_players(self.board_controller.map)
            self.board_controller.execute_orders(orders)
