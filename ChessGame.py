import pygame
from Board import Board

class ChessGame:

    def __init__(self, window_size):
        pygame.init()
        self.board = Board()
        self.screen = pygame.display.set_mode(window_size)
        self.square_size = (window_size[0] / 8, window_size[1] / 8)
        pygame.display.update()
        self.draw_board()
        pygame.display.update()
        self.current_colour = 'black'
        self.game_loop()
        self.checkmate_moves = []

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                if self.board.board[i][j] is not None:
                    image = pygame.image.load(self.board.board[i][j].sprite)
                    image = image.convert_alpha()
                    self.screen.blit(image, (i * self.square_size[0], j * self.square_size[1]))

    def draw_board(self):
        for i in range(8):
            if i % 2 == 0:
                colour = (139, 69, 19)
            else:
                colour = (255, 248, 220)
            for j in range(8):
                if colour == (139, 69, 19):
                    colour = (255, 248, 220)
                else:
                    colour = (139, 69, 19)
                pygame.draw.rect(self.screen, colour, (
                j * self.square_size[0], i * self.square_size[1], self.square_size[0], self.square_size[1]))
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
                print('click')
                (pos_x, pos_y) = pygame.mouse.get_pos()
                pos_x = int(pos_x // self.square_size[0])
                pos_y = int(pos_y // self.square_size[1])
                # print((pos_x, pos_y), currently_selected_moves)
                if currently_selected is None:
                    self.draw_board()

                    if self.board.board[pos_x][pos_y] is not None and self.board.board[pos_x][pos_y].colour == self.current_colour:
                        currently_selected = self.board.board[pos_x][pos_y]
                        currently_selected_moves = self.board.board[pos_x][pos_y].get_moves(self.board, (pos_x, pos_y))
                        current_piece_pos = (pos_x, pos_y)
                        for (x, y) in currently_selected_moves:
                            pygame.draw.rect(self.screen, (0, 255, 0), (
                            (pos_x + x) * self.square_size[0], (pos_y + y) * self.square_size[1], self.square_size[0],
                            self.square_size[1]))
                            self.draw_pieces()
                elif currently_selected is not None and currently_selected_moves is not None and current_piece_pos is not None:
                    # move another piece
                    if self.board.board[pos_x][pos_y] is not None and self.board.board[pos_x][pos_y].colour == self.current_colour:
                        print('switching')
                        currently_selected = self.board.board[pos_x][pos_y]
                        currently_selected_moves = self.board.board[pos_x][pos_y].get_moves(self.board, (pos_x, pos_y))
                        current_piece_pos = (pos_x, pos_y)
                        self.draw_board()
                        for (x, y) in currently_selected_moves:
                            pygame.draw.rect(self.screen, (0, 255, 0), (
                                (pos_x + x) * self.square_size[0], (pos_y + y) * self.square_size[1],
                                self.square_size[0], self.square_size[1]))
                            self.draw_pieces()
                    for move in currently_selected_moves:
                        #print(current_piece_pos)
                        if (current_piece_pos[0] + move[0], current_piece_pos[1] + move[1]) == (pos_x, pos_y):
                            self.board.board[pos_x][pos_y] = currently_selected
                            self.board.board[current_piece_pos[0]][current_piece_pos[1]] = None
                            currently_selected.has_moved = True
                            currently_selected = None
                            currently_selected_moves = None
                            self.draw_board()
                            if self.current_colour == 'white':
                                self.current_colour = 'black'
                                print('Black turn')
                            else:
                                self.current_colour = 'white'
                                print('White turn')

                            if self.board.is_checkmate(self.current_colour, self.board, 0):
                                print('checkmate')



ChessGame((500,500))