from stockfish import Stockfish

class Board:
    def __init__(self, binary_path: str, num_players: str) -> None:
        self.stockfish = Stockfish(path=binary_path)
        self.turn = 'White'
        self.set_number_of_players(num_players)

    def set_number_of_players(self, num_players):
        self.num_players = num_players
        if num_players == '1':
            self.get_elo_rating()
        else:
            self.get_player_names()

    def get_player_names(self):
        white_name = input('White Player Name: ')
        black_name = input('Black Player Name: ')
        self.white_name = white_name
        self.black_name = black_name

    def get_elo_rating(self):
        elo_rating = input('Please type in your ELO rating: ')
        self.stockfish.set_elo_rating(elo_rating)

    def change_turn(self):
        if self.turn == 'White':
            self.turn = 'Black'
        else:
            self.turn = 'White'

    def get_pos(self):
        print(self.stockfish.get_board_visual())
        return

    def check_move(self, move: str):
        check_move = self.stockfish.is_move_correct(move)
        return check_move

    def input_move(self, move: str):
        if self.num_players == '1':
            print(f'{self.turn} plays: {move}')
        else:
            if self.turn == 'White':
                print(f'{self.white_name} plays: {move}')
            else:
                print(f'{self.black_name} plays: {move}')
  
        new_move = self.stockfish.make_moves_from_current_position([move])
        self.change_turn()
        return new_move

    def make_cpu_move(self, wtime: str = None, btime: str = None):
        cpu_move = self.stockfish.get_best_move()
        print(f'{self.turn}\'s move: ', cpu_move)
        new_move = self.stockfish.make_moves_from_current_position([cpu_move])
        self.change_turn()
        return new_move

    def get_top_moves(self, number_of_moves: int):
        top_moves = self.stockfish.get_top_moves(number_of_moves)
        return top_moves