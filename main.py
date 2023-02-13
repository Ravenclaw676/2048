from Board import Board

board = Board()
print(board.add_block())
print(board.add_block())

board.merge_block(0, 0, 1, 0)
print(board)
