class Piece:

    def __init__(self, type, sprite, colour):
        self.type = type
        self.sprite = sprite
        self.colour = colour

    def move_is_valid(self, board, move, pos):
        final_x = pos[0] + move[0]
        final_y = pos[1] + move[1]

        if not (0 <= final_x < 8 and 0 <= final_y < 8):
            return False
        if board[final_x][final_y] is not None:
            if board[final_x][final_y].colour == self.colour:
                return False

        # TODO: Implement checking if the move is blocked

        return True

    def get_moves(self, board, pos):
        moves = []

        if self.type == 'pawn':

            if self.colour == 'white':
                moves.append((0, 1))
                if pos[0] > 0 and pos[1] < 8 and board[pos[0]-1][pos[1]+1] is not None and board[pos[0]-1][pos[1]+1].colour != self.colour:
                    moves.append((-1, 1))
                    print('can cap left')
                if pos[0] < 7 and pos[1] < 8 and board[pos[0]+1][pos[1]+1] is not None and board[pos[0]+1][pos[1]+1].colour != self.colour:
                    moves.append((1, 1))
                    print('can cap right')
            else:
                moves.append((0, -1))
                if pos[0] > 0 and pos[1] > 0 and board[pos[0]-1][pos[1]-1] is not None and board[pos[0]-1][pos[1]-1].colour != self.colour:
                    moves.append((-1, -1))
                    print('can cap left')
                if pos[0] < 7 and pos[1] > 0 and board[pos[0]+1][pos[1]-1] is not None and board[pos[0]+1][pos[1]-1].colour != self.colour:
                    moves.append((1, -1))
                    print('can cap right')

        if self.type == 'rook':
            for i in range(-7, 8):
                moves.append((i,0))
                moves.append((0,i))

        if self.type == 'bishop':
            for i in range(-7,8):
                moves.append((i,i))
                moves.append((i, i*-1))

        if self.type == 'knight':
            moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        if self.type == 'queen':
            for i in range(-7,8):
                moves.append((i,0))
                moves.append((0,i))
                moves.append((i,i))
                moves.append((i, i*-1))

        if self.type == 'king':
            moves = [(1,1),(1,0),(0,1),(-1,1),(1,-1),(0,-1),(-1,0),(-1,-1)]

        removed = []
        for move in moves:
            if not self.move_is_valid(board, move, pos):
                removed.append(move)

        for move in removed:
            moves.remove(move)

        return moves
