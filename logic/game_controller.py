from input.base_io_controller import BaseIOController
from .board_controller import BoardController


class GameController:

    def __init__(self, input_controller: BaseIOController):
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
            orders = self.input_controller.propagate_board_state(self.board_controller.board)
            self.board_controller.execute_orders(orders)
