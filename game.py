from logic.game_controller import GameController
from input.tcp_io_controller import TCPIOController

import sys

if __name__ == "__main__":
    player_count = " ".join(sys.argv[1:])
    game_controller = GameController(TCPIOController(int(player_count)))



