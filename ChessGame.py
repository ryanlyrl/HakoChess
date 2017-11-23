import pygame
from Board import Board

class ChessGame:

    def __init__(self, window_size):
        self.board = Board(window_size)

    def start(self):
        pass
        # self.do_turn(0)

    # def do_turn(self, colour):


ChessGame((500,500))