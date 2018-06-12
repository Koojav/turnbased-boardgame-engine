import array


class BoardState:
    def __init__(self):
        # TODO: Consider renaming "id" to "turn" - maybe will clear up some naming stuff in TCPServer ?
        self.id = 0
        self.state = BoardState.generate_fresh_state(100, 10)

    @staticmethod
    def generate_fresh_state(width, height):
        # TODO: Take actual width and height into account
        return array.array('B', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
