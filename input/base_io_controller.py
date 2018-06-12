from logic.board_state import  BoardState


class BaseIOController:
    def __init__(self, player_count: int):
        self.player_count = player_count

    def start(self):
        raise NotImplementedError

    def propagate_board_state(self, board_state: BoardState):
        raise NotImplementedError
