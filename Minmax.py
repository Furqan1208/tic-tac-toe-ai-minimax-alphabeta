import time
import copy

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        print()
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def print_board_nums(self):
        print()
        number_board = [[str(i) for i in range(j, j+3)] for j in range(0, 9, 3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            diag2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diag1]) or all([spot == letter for spot in diag2]):
                return True

        return False

def minimax(board, is_maximizing, player, opponent):
    if board.current_winner == player:
        return 1
    elif board.current_winner == opponent:
        return -1
    elif not board.empty_squares():
        return 0

    if is_maximizing:
        best = -float('inf')
        for move in board.available_moves():
            new_board = copy.deepcopy(board)
            new_board.make_move(move, player)
            score = minimax(new_board, False, player, opponent)
            best = max(score, best)
        return best
    else:
        best = float('inf')
        for move in board.available_moves():
            new_board = copy.deepcopy(board)
            new_board.make_move(move, opponent)
            score = minimax(new_board, True, player, opponent)
            best = min(score, best)
        return best

def minimax_ab(board, depth, alpha, beta, is_maximizing, player, opponent):
    if board.current_winner == player:
        return 1
    elif board.current_winner == opponent:
        return -1
    elif not board.empty_squares():
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in board.available_moves():
            new_board = copy.deepcopy(board)
            new_board.make_move(move, player)
            eval = minimax_ab(new_board, depth+1, alpha, beta, False, player, opponent)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.available_moves():
            new_board = copy.deepcopy(board)
            new_board.make_move(move, opponent)
            eval = minimax_ab(new_board, depth+1, alpha, beta, True, player, opponent)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, player, opponent, use_alpha_beta=False):
    best_score = -float('inf')
    best_move = None
    for move in board.available_moves():
        temp_board = copy.deepcopy(board)
        temp_board.make_move(move, player)
        if use_alpha_beta:
            score = minimax_ab(temp_board, 0, -float('inf'), float('inf'), False, player, opponent)
        else:
            score = minimax(temp_board, False, player, opponent)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def compare_performance():
    rounds = 3  # Reduced for faster comparison
    time_minimax = 0
    time_alpha_beta = 0

    for i in range(rounds):
        print(f"Running test {i+1}/{rounds}...")

        board1 = TicTacToe()
        board2 = TicTacToe()

        start = time.time()
        get_best_move(board1, 'X', 'O', use_alpha_beta=False)
        time_minimax += time.time() - start

        start = time.time()
        get_best_move(board2, 'X', 'O', use_alpha_beta=True)
        time_alpha_beta += time.time() - start

    print("\nPerformance Comparison:")
    print(f"Minimax Avg Time: {time_minimax / rounds:.6f} seconds")
    print(f"Alpha-Beta Avg Time: {time_alpha_beta / rounds:.6f} seconds")

def play_game(use_alpha_beta=False):
    game = TicTacToe()
    player_letter = 'O'
    ai_letter = 'X'

    game.print_board_nums()

    while game.empty_squares():
        # Human move
        move = None
        while move not in game.available_moves():
            try:
                move = int(input("Your move (0-8): "))
            except:
                print("Invalid input. Enter a number 0-8.")
        game.make_move(move, player_letter)
        game.print_board()

        if game.current_winner:
            print("You win!")
            break

        if not game.empty_squares():
            print("It's a tie!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = get_best_move(game, ai_letter, player_letter, use_alpha_beta)
        game.make_move(ai_move, ai_letter)
        game.print_board()

        if game.current_winner:
            print("AI wins!")
            break

        if not game.empty_squares():
            print("It's a tie!")
            break

if __name__ == '__main__':
    print("Welcome to Tic Tac Toe vs AI!")
    print("You are O, AI is X.")
    mode = input("Use Alpha-Beta Pruning? (y/n): ").lower().strip() == 'y'
    play_game(use_alpha_beta=mode)

    run_perf = input("\nRun performance comparison? (y/n): ").lower().strip() == 'y'
    if run_perf:
        compare_performance()
