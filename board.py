import math
import random
from random import randint 
import time
import readFile
import attackCount

board_size = 8
files = 'abcdefgh'
ranks = '12345678'

def pick_random_location():
    """Returns a random tuple containing row and col information."""
    row = random.randrange(board_size)
    col = random.randrange(board_size)

    random_location = row, col

    return random_location

def is_overlapping(pieces, new_piece_location):
    """Returns True if the new piece overlaps with an existing one."""
    new_row, new_col = new_piece_location

    for piece in pieces:
        __, __, row, col = piece
        if row == new_row and col == new_col:
            return True

    return False

def pick_free_location(pieces):
    """Returns a random location with no existing piece."""
    free_location = pick_random_location()

    while is_overlapping(pieces, free_location):
        free_location = pick_random_location()

    return free_location

def initialize_board(piece_groups):
    """Initialize the board with chess pieces at random locations.

    Accepts piece_groups. Returns a list of 4-tuples that contains:
    the piece's color, its type, its row, and its column.
    It is guaranteed that the location of each piece will not overlap
    (assuming total number of pieces < board_size^2).
    """
    pieces = []

    for piece_group in piece_groups:
        color, piece_type, amount = piece_group

        for i in range(amount):
            row, col = pick_free_location(pieces)

            pieces.append((color, piece_type, row, col))

    return pieces

def draw_board(pieces):
    """Returns the string representation of a board's instance.

    Blank squares are represented by dots (.).
    White pieces are represented by capital letters.
    Black pieces are represented by lowercase letters.
    """
    board = []

    # build a matrix with all cell filled with dots (.)
    for i in range(board_size):
        board_row = []

        for j in range(board_size):
            board_row.append('.')

        board.append(board_row)

    # replace some dots with the actual pieces
    for piece in pieces:
        color, piece_type, row, col = piece

        if color == 'white':
            board[row][col] = piece_type.upper()[0]
        elif color == 'black':
            board[row][col] = piece_type[0]
        else:
            raise ValueError

    board_string = ''

    # format the output to make it pretty
    for i in range(board_size + 1):
        for j in range(-1, board_size):
            if i == board_size:
                if j == -1:
                    board_string += ' '
                else:
                    board_string += ' ' + files[j]
            elif j == -1:
                board_string += ranks[7 - i]
            else:
                board_string += ' ' + board[7 - i][j]
        board_string += '\n'

    return board_string