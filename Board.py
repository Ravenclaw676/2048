"""a file that contains the Board class"""

from random import randint, choice


class Board():
    """a class that is the game board"""
    def __init__(self):
        self.grid = [
            [5, 5, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.score = 0
        self.__possible_blocks = (2, 4)

    def __str__(self):
        self.set_score()

        string = f"score: {self.score}\n"
        string += f"{self.grid[0]}\n"
        string += f"{self.grid[1]}\n"
        string += f"{self.grid[2]}\n"
        string += f"{self.grid[3]}\n"

        return string

    def get_value(self, board_x, board_y):
        """returns the number held a board x, y"""
        return self.grid[board_y][board_x]

    def get_score(self):
        """"returns the score"""
        return self.score

    def set_score(self):
        """updates the score"""
        self.score = 0
        for row in self.grid:
            for block in row:
                self.score += block

    def add_block(self):
        """adds block from possible blocks to a random square"""
        block_x = randint(0, 3)
        block_y = randint(0, 3)
        while self.grid[block_y][block_x] != 0:
            block_x = randint(0, 3)
            block_y = randint(0, 3)
        self.grid[block_y][block_x] = choice(self.__possible_blocks)

        return self

    def merge_block(self, stationary_x, stationary_y, moving_x, moving_y):
        """It merges 2 adjacent blocks"""
        location = self.grid[stationary_y][stationary_x]
        if location == self.grid[moving_y][moving_x]:
            location *= 2
            self.grid[moving_y][moving_x] = 0
