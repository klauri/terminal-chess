from time import sleep
from Board import Board


stockfish_config = {
    "path": '/usr/games/stockfish',
    "Debug Log File": "/log.txt",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Threads": 1, # More threads will make the engine stronger, but should be kept at less than the number of logical processors on your computer.
    "Ponder": "false",
    "Hash": 16, # Default size is 16 MB. It's recommended that you increase this value, but keep it as some power of 2. E.g., if you're fine using 2 GB of RAM, set Hash to 2048 (11th power of 2).
    "MultiPV": 1,
    "Skill Level": 20,
    "Move Overhead": 10,
    "Minimum Thinking Time": 20,
    "Slow Mover": 100,
    "UCI_Chess960": "false",
    "UCI_LimitStrength": "false",
    "UCI_Elo": 1350
}


if __name__ == '__main__':
    game_running = True

    print('Welcome to Chess!')
    print('\n\n')
    print('Capital letters represent White, lowercase represent Black')
    print('\n')
    print('Input your moves in Coordinate Notation')
    print('Example: \"e2e4\"')

    print('\n\n')
    print('Type \'help\' for the top 3 moves.')
    print('\n\n')
    input('Press Enter to start a new game...')

    board = Board(binary_path='/usr/games/stockfish')

    elo_rating = input('Please type in your ELO rating: ')
    board.stockfish.set_elo_rating(elo_rating)

    board.get_pos()

    while game_running:
        print(board.turn)
        new_move = ''

        new_move = input('Move: ')

        if new_move == 'help':
            print(board.get_top_moves(3))

        check_move = board.check_move(new_move)
        if not check_move: 
            print('Invald move! Try again. ')
        else:
            board.input_move(new_move)
            board.get_pos()
            print('Waiting for opponent...')
            board.make_cpu_move()
            board.get_pos()

