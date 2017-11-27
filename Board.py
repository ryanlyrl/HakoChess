import pygame
from Piece import Piece


class Board:

    def __init__(self, window_size):
        pygame.init()
        self.board = [[None for i in range(8)] for j in range(8)]
        self.screen = pygame.display.set_mode(window_size)
        self.square_size = (window_size[0] / 8, window_size[1] / 8)
        pygame.display.update()

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

        self.draw_board()
        pygame.display.update()
        self.game_loop()

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    image = pygame.image.load(self.board[i][j].sprite)
                    image = image.convert_alpha()
                    self.screen.blit(image, (i*self.square_size[0], j*self.square_size[1]))

    def draw_board(self):
        for i in range(8):
            if i % 2 == 0:
                colour = (139,69,19)
            else:
                colour = (255,248,220)
            for j in range(8):
                if colour == (139,69,19):
                    colour = (255,248,220)
                else:
                    colour = (139,69,19)
                pygame.draw.rect(self.screen, colour, (j* self.square_size[0], i * self.square_size[1], self.square_size[0], self.square_size[1]))
        self.draw_pieces()
        pygame.display.update()

    def game_loop(self):
        currently_selected = None
        currently_selected_moves = None
        current_piece_pos = None
        while True:
            pygame.display.update()
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (pos_x, pos_y) = pygame.mouse.get_pos()
                pos_x = int(pos_x // self.square_size[0])
                pos_y = int(pos_y // self.square_size[1])
                #print((pos_x, pos_y), currently_selected_moves)
                if currently_selected is None:
                    self.draw_board()

                    if self.board[pos_x][pos_y] is not None:
                        currently_selected = self.board[pos_x][pos_y]
                        currently_selected_moves = self.board[pos_x][pos_y].get_moves(self.board, (pos_x, pos_y))
                        current_piece_pos = (pos_x, pos_y)
                        for (x,y) in currently_selected_moves:
                            pygame.draw.rect(self.screen, (0,255,0), ((pos_x + x) * self.square_size[0], (pos_y + y) * self.square_size[1], self.square_size[0], self.square_size[1]))
                            self.draw_pieces()
                elif currently_selected is not None and currently_selected_moves is not None and current_piece_pos is not None:
                    for move in currently_selected_moves:
                        print(current_piece_pos)
                        if (current_piece_pos[0] + move[0], current_piece_pos[1] + move[1]) == (pos_x, pos_y):
                            self.board[pos_x][pos_y] = currently_selected
                            self.board[current_piece_pos[0]][current_piece_pos[1]] = None
                            currently_selected = None
                            currently_selected_moves = None
                            self.draw_board()