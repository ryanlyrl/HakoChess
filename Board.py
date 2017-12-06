import pygame
from Piece import Piece


class Board:

    def __init__(self, board=None):
        self.board = [[None for i in range(8)] for j in range(8)]

        if board:
            self.board = board
        else:
            # White pieces
            # pawns
            for i in range(8):
                self.board[i][1] = Piece('pawn', 'white_pawn.png', 'white')
            self.board[0][0] = Piece('rook', 'white_rook.png', 'white')
            self.board[1][0] = Piece('knight', 'white_knight.png', 'white')
            self.board[2][0] = Piece('bishop', 'white_bishop.png', 'white')
            self.board[3][0] = Piece('king', 'white_king.png', 'white')
            self.board[4][0] = Piece('queen', 'white_queen.png', 'white')
            self.board[5][0] = Piece('bishop', 'white_bishop.png', 'white')
            self.board[6][0] = Piece('knight', 'white_knight.png', 'white')
            self.board[7][0] = Piece('rook', 'white_rook.png', 'white')

            # black pieces
            for i in range(8):
                self.board[i][6] = Piece('pawn', 'black_pawn.png', 'black')
            self.board[0][7] = Piece('rook', 'black_rook.png', 'black')
            self.board[1][7] = Piece('knight', 'black_knight.png', 'black')
            self.board[2][7] = Piece('bishop', 'black_bishop.png', 'black')
            self.board[3][7] = Piece('king', 'black_king.png', 'black')
            self.board[4][7] = Piece('queen', 'black_queen.png', 'black')
            self.board[5][7] = Piece('bishop', 'black_bishop.png', 'black')
            self.board[6][7] = Piece('knight', 'black_knight.png', 'black')
            self.board[7][7] = Piece('rook', 'black_rook.png', 'black')

    def is_checkmate(self, colour, board, depth):
        opponent_possible_moves = []
        player_possible_moves = []
        king_pos = ()
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece is not None:
                    if piece.colour != colour:
                        moves = piece.get_moves(board, (i, j))
                        for move in moves:
                            opponent_possible_moves.append((move[0] + i, move[1] + j))
                    else:
                        moves = piece.get_moves(board, (i, j))
                        for move in moves:
                            player_possible_moves.append((move[0] + i, move[1] + j))
                    if piece.colour == colour and piece.type == 'king':
                        king_pos = (i, j)

        king = board[king_pos[0]][king_pos[1]]
        if king_pos in opponent_possible_moves:
            print('check')
            for move in king.get_moves(board, (king_pos[0], king_pos[1])):
                if (king_pos[0] + move[0], king_pos[1] + move[1]) not in opponent_possible_moves:
                    return False
            if depth == 0:
                for move in player_possible_moves:
                    test_board = Board(self.board)
                    test_board[move[0]][move[1]] = None
                    if not self.is_checkmate(colour, test_board, 1):
                        return False
                    print('can kill to escape')
            print('checkmate')
            return True
        else:
            return True
