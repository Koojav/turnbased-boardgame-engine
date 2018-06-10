from logic.game_controller import GameController
from input.tcp_input_controller import TCPInputController

import sys

if __name__ == "__main__":
    player_count = " ".join(sys.argv[1:])
    # TODO: Make sure this doesn't exit until I don't know when honestly...
    game_controller = GameController(TCPInputController(int(player_count)))



