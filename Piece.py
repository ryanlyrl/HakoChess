class Piece:

    def __init__(self, type, sprite, colour):
        self.type = type
        self.sprite = sprite
        self.colour = colour
        self.has_moved = False

    def move_is_valid(self, board, move, pos):
        final_x = pos[0] + move[0]
        final_y = pos[1] + move[1]

        if not (0 <= final_x < 8 and 0 <= final_y < 8):
            return False
        if board[final_x][final_y] is not None:
            if board[final_x][final_y].colour == self.colour:
                return False

        return True

    def blocked_moves(self, board, pos, moves):
        print('block called')
        if self.type == 'knight' or self.type == 'king':
            return moves

        print('checking')

        valid_moves = []
        print(pos)

        if self.type == 'pawn':
            if self.colour == 'white':
                if board[pos[0]][pos[1]+1] is not None and (0,1) in moves:
                    moves.remove((0, 1))
                    if (0,2) in moves:
                        moves.remove((0, 2))
                        return moves
                if board[pos[0]][pos[1]+2] is not None and (0,2) in moves:
                    moves.remove((0, 2))
            else:
                if board[pos[0]][pos[1]-1] is not None and (0,-1) in moves:
                    moves.remove((0, -1))
                    if not self.has_moved and (0,-2) in moves:
                        moves.remove((0, -2))
                        return moves
                if board[pos[0]][pos[1]-2] is not None and (0,2) in moves:
                    moves.remove((0, -2))
            return moves

        if self.type == 'rook' or self.type == 'queen':
            for i in range(pos[1] - 1, -1, -1):
                if board[pos[0]][i] is None:
                    valid_moves.append((pos[0], i))
                elif board[pos[0]][i].colour != self.colour:
                    valid_moves.append((pos[0],i))
                    break
                else:
                    break
            for i in range(pos[1] + 1, 8):
                if board[pos[0]][i] is None:
                    valid_moves.append((pos[0], i))
                elif board[pos[0]][i].colour != self.colour:
                    valid_moves.append((pos[0], i))
                    break
                else:
                    break
            for i in range(pos[0] - 1, -1, -1):
                if board [i][pos[1]] is None:
                    valid_moves.append((i, pos[1]))
                elif board[i][pos[1]].colour != self.colour:
                    valid_moves.append((i, pos[1]))
                    break
                else:
                    break
            for i in range(pos[0] + 1, 8):
                if board[i][pos[1]] is None:
                    valid_moves.append((i, pos[1]))
                elif board[i][pos[1]].colour != self.colour:
                    valid_moves.append((i, pos[1]))
                    break
                else:
                    break

        if self.type == 'bishop' or self.type == 'queen':
            x = pos[0] + 1; y = pos[1] + 1
            while x < 8 and y < 8:
                if board[x][y] is None:
                    valid_moves.append((x,y))
                elif board[x][y].colour != self.colour:
                    valid_moves.append((x,y))
                    break
                else:
                    break
                x += 1; y += 1
            x = pos[0] - 1; y = pos[1] + 1
            while x >= 0 and y < 8:
                if board[x][y] is None:
                    valid_moves.append((x,y))
                elif board[x][y].colour != self.colour:
                    valid_moves.append((x, y))
                    break
                else:
                    break
                x -= 1; y += 1
            x = pos[0] - 1; y = pos[1] - 1
            while x >= 0 and y >= 0:
                if board[x][y] is None:
                    valid_moves.append((x,y))
                elif board[x][y].colour != self.colour:
                    valid_moves.append((x, y))
                    break
                else:
                    break
                x -= 1; y -= 1
            x = pos[0] + 1; y = pos[1] - 1
            while x < 8 and y >= 0:
                if board[x][y] is None:
                    valid_moves.append((x,y))
                elif board[x][y].colour != self.colour:
                    valid_moves.append((x, y))
                    break
                else:
                    break
                x += 1; y -= 1

        move_output = []
        print('valid',valid_moves)
        for move in moves:
            if (pos[0] + move[0], pos[1] + move[1]) in valid_moves:
                move_output.append(move)
        return move_output

    def get_moves(self, board, pos):
        moves = []

        if self.type == 'pawn':

            if self.colour == 'white':
                if not self.has_moved:
                    moves.append((0, 2))
                moves.append((0, 1))
                if pos[0] > 0 and pos[1] < 8 and board[pos[0]-1][pos[1]+1] is not None and board[pos[0]-1][pos[1]+1].colour != self.colour:
                    moves.append((-1, 1))
                    print('can cap left')
                if pos[0] < 7 and pos[1] < 8 and board[pos[0]+1][pos[1]+1] is not None and board[pos[0]+1][pos[1]+1].colour != self.colour:
                    moves.append((1, 1))
                    print('can cap right')
            else:
                if not self.has_moved:
                    moves.append((0, -2))
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

        moves = self.blocked_moves(board, pos, moves)

        print('Moves: ' + str(moves))
        return moves