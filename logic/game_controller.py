from .board_controller import BoardController
import threading


class GameController:

    def __init__(self, input_controller_class, player_count):
        self.input_controller = input_controller_class(player_count)
        input_controller_thread = threading.Thread(target=self.input_controller.start)
        input_controller_thread.start()

        self.board_controller = BoardController()

        # Game's main loop
        self.main_loop()

        # input_controller_thread.join()

    def execute_orders(self):
        pass

    def broadcast_map_state(self):
        pass

    def main_loop(self):
        while True:
            orders = self.input_controller.wait_for_all_orders()
            new_board_state = self.board_controller.execute_orders(orders)
            self.input_controller.propagate_board_state(new_board_state)

