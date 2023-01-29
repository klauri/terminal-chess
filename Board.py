from stockfish import Stockfish

class Board:
    def __init__(self, binary_path) -> None:
        self.stockfish = Stockfish(path=binary_path)
        self.turn = 'white'
        self.get_pos()

    def get_pos(self):
        print(self.stockfish.get_board_visual())
        return

    def check_move(self, move: str):
        check_move = self.stockfish.is_move_correct(move)
        return check_move

    def input_move(self, move: str):
        new_move = self.stockfish.make_moves_from_current_position([move])
        return new_move

    def make_cpu_move(self, wtime: str = None, btime: str = None):
        cpu_move = self.stockfish.get_best_move()
        new_move = self.stockfish.make_moves_from_current_position([cpu_move])
        return new_move