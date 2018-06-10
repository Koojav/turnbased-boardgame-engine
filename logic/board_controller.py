from .board_state import BoardState


class BoardController:
    def __init__(self):
        self.board_state = BoardState()

    def execute_orders(self, orders: list):
        # TODO: modifies self.board_state according to received orders
        return self.board_state


