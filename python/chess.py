# import numpy as np
from numba import jit

# Piece representations
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

# Colors
WHITE = 0
BLACK = 1

class ChessEngine:
    def __init__(self):
        self.board = np.zeros((8, 8, 2), dtype=np.int8)
        self.initialize_board()
        self.current_player = WHITE
        
    def initialize_board(self):
        # Initialize pawns
        self.board[1, :, WHITE] = PAWN
        self.board[6, :, BLACK] = PAWN
        
        # Initialize other pieces
        back_rank = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        self.board[0, :, WHITE] = back_rank
        self.board[7, :, BLACK] = back_rank

    @staticmethod
    @jit(nopython=True)
    def evaluate_position(board):
        # Piece values
        piece_values = [0, 100, 320, 330, 500, 900, 20000]
        
        # Simple material-based evaluation
        score = 0
        for i in range(8):
            for j in range(8):
                piece_white = board[i, j, WHITE]
                piece_black = board[i, j, BLACK]
                score += piece_values[piece_white] - piece_values[piece_black]
        
        return score

    @staticmethod
    @jit(nopython=True)
    def generate_moves(board, player):
        moves = []
        for i in range(8):
            for j in range(8):
                piece = board[i, j, player]
                if piece != EMPTY:
                    if piece == PAWN:
                        # Pawn move generation
                        direction = 1 if player == WHITE else -1
                        if 0 <= i + direction < 8 and board[i + direction, j, 1-player] == EMPTY:
                            moves.append((i, j, i + direction, j))
                        # Add other pawn moves (double move, captures, en passant)
                    # Add move generation for other pieces
        return moves

    @staticmethod
    @jit(nopython=True)
    def make_move(board, move):
        start_row, start_col, end_row, end_col = move
        board[end_row, end_col] = board[start_row, start_col]
        board[start_row, start_col] = 0
        return board

    @staticmethod
    @jit(nopython=True)
    def alpha_beta(board, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return ChessEngine.evaluate_position(board)
        
        if maximizing_player:
            max_eval = -np.inf
            for move in ChessEngine.generate_moves(board, WHITE):
                new_board = ChessEngine.make_move(board.copy(), move)
                eval = ChessEngine.alpha_beta(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = np.inf
            for move in ChessEngine.generate_moves(board, BLACK):
                new_board = ChessEngine.make_move(board.copy(), move)
                eval = ChessEngine.alpha_beta(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, depth):
        best_move = None
        best_eval = -np.inf if self.current_player == WHITE else np.inf
        alpha = -np.inf
        beta = np.inf
        
        for move in self.generate_moves(self.board, self.current_player):
            new_board = self.make_move(self.board.copy(), move)
            eval = self.alpha_beta(new_board, depth - 1, alpha, beta, self.current_player == BLACK)
            
            if self.current_player == WHITE and eval > best_eval:
                best_eval = eval
                best_move = move
            elif self.current_player == BLACK and eval < best_eval:
                best_eval = eval
                best_move = move
            
            if self.current_player == WHITE:
                alpha = max(alpha, eval)
            else:
                beta = min(beta, eval)
            
            if beta <= alpha:
                break
        
        return best_move

# Usage example
engine = ChessEngine()
best_move = engine.get_best_move(depth=4)
print(f"Best move: {best_move}")