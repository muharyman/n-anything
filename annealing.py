import math
import random
import time

board_size = 8
files = 'abcdefgh'
ranks = '12345678'

def read_input(filename='input.txt'):
    """Reads input from file and returns a list of piece groups.

    Returns a list of 3-tuples representing the piece groups.
    Each tuple contains the piece group's color, its type, and its
    amount.
    """
    piece_groups = []

    with open(filename) as f:
        for line in f:
            line = line.strip()
            words = line.split(sep=' ')
            words = [word.lower() for word in words]

            color, piece_type, amount = words
            amount = int(amount)

            piece_groups.append((color, piece_type, amount))

    return piece_groups

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

def find_piece_at(pieces, row, col):
    """Returns the piece information at specified row and col."""
    for piece in pieces:
        __, __, piece_row, piece_col = piece

        if piece_row == row and piece_col == col:
            return piece

def is_inside_board(row, col):
    """Returns true if the location is inside the board."""
    return row in range(board_size) and col in range(board_size)


def count_pieces_attacked_by(pieces, piece):
    """Return the number of pieces attacked by piece.

    Returns a 2-tuple containing the number of pieces that is attacked:
    First number represents the number of attacked pieces with the same
    color.
    Second number represents the number of attacked pieces with
    different color.
    """
    piece_color, piece_type, piece_row, piece_col = piece
    location = piece_row, piece_col

    same_color_attacks = 0
    different_color_attacks = 0

    if piece_type == 'knight':
        # list all reachable squares
        reachable_squares = []
        deltas = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        for delta in deltas:
            new_location = tuple(sum(x) for x in zip(location, delta))

            if is_inside_board(*new_location):
                reachable_squares.append(new_location)

        # if found an existing piece at a reachable squares, add it to
        # the attacks count
        for new_row, new_col in reachable_squares:
            attacked_piece = find_piece_at(pieces, new_row, new_col)

            if attacked_piece:
                attacked_color, __, __, __ = attacked_piece

                if attacked_color == piece_color:
                    same_color_attacks += 1
                else:
                    different_color_attacks += 1

    else:
        if piece_type == 'bishop':
            deltas = [
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]

        elif piece_type == 'rook':
            deltas = [
                (-1, 0), (0, -1), (0, 1), (1, 0)
            ]

        elif piece_type == 'queen':
            deltas = [
                (-1, -1), (-1, 1), (1, -1), (1, 1),
                (-1, 0), (0, -1), (0, 1), (1, 0)
            ]
        else:
            raise ValueError

        # for every direction specified with the delta
        for delta in deltas:
            new_location = tuple(sum(x) for x in zip(location, delta))
            attacked_piece = find_piece_at(pieces, *new_location)

            # move in one direction until found a piece or until the
            # edge of the board is reached
            while is_inside_board(*new_location) and not attacked_piece:
                new_location = tuple(sum(x) for x in zip(new_location, delta))
                attacked_piece = find_piece_at(pieces, *new_location)

            if attacked_piece:
                attacked_color, __, __, __ = attacked_piece

                if attacked_color == piece_color:
                    same_color_attacks += 1
                else:
                    different_color_attacks += 1

    attacks_count = same_color_attacks, different_color_attacks

    return attacks_count

def count_all_attacks(pieces):
    """Returns all attacks by all pieces.

    Returns a 2-tuple:
    First element of the tuple is the total number of attacks made by
    pieces with same color (white-attacks-white or black-attacks-black).
    Second element of the tuple is the total number of attacks made by
    pieces with different color (white-attacks-black and vice versa).
    """
    same_color_total = 0
    different_color_total = 0

    for piece in pieces:
        attacks_count = count_pieces_attacked_by(pieces, piece)
        same_color_attacks, different_color_attacks = attacks_count
        same_color_total += same_color_attacks
        different_color_total += different_color_attacks

    total_attacks_count = same_color_total, different_color_total

    return total_attacks_count

def select_with_probability(probability):
    """Within the specified probability, returns True."""
    return random.random() < probability

def format_piece(piece):
    """Returns a tuple with a (color, type, rank, file) format."""
    color, piece_type, row, col = piece
    return color, piece_type, files[col], ranks[row]

def hill_climbing(pieces):
    """Solves the n-ything problem with hill-climbing algorithm."""
    total_same, total_different = count_all_attacks(pieces)

    max_stuck = 1000
    stuck_counter = 0
    while True:
        piece_to_be_moved = random.choice(pieces)
        color, piece_type, __, __ = piece_to_be_moved

        new_location = pick_free_location(pieces)
        new_piece = color, piece_type, *new_location

        new_pieces = pieces.copy()
        new_pieces.remove(piece_to_be_moved)
        new_pieces.append(new_piece)
        new_total_same, new_total_different = count_all_attacks(new_pieces)

        better_value = (
            new_total_same < total_same and new_total_different > total_different
            or
            new_total_same < total_same and new_total_different == total_different
            or
            new_total_same == total_same and new_total_different > total_different
        )

        same_value = (
            new_total_same == total_same and new_total_different == total_different
        )

        if better_value:
            pieces = new_pieces
            total_same, total_different = new_total_same, new_total_different
            stuck_counter = 0
        elif same_value:
            pieces = new_pieces
            stuck_counter += 1
        else:
            stuck_counter += 1

        if stuck_counter == max_stuck:
            break

    return pieces

def simulated_annealing(pieces, steps=1000, temperature=1, rate=10):
    """Solves the n-ything problem with simulated annealing."""
    total_same, total_different = count_all_attacks(pieces)

    for i in range(steps):
        piece_to_be_moved = random.choice(pieces)
        color, piece_type, __, __ = piece_to_be_moved

        new_location = pick_free_location(pieces)
        new_piece = color, piece_type, *new_location

        new_pieces = pieces.copy()
        new_pieces.remove(piece_to_be_moved)
        new_pieces.append(new_piece)
        new_total_same, new_total_different = count_all_attacks(new_pieces)

        better_value = (
            new_total_same < total_same and new_total_different > total_different
            or
            new_total_same < total_same and new_total_different == total_different
            or
            new_total_same == total_same and new_total_different > total_different
        )

        same_value = (
            new_total_same == total_same and new_total_different == total_different
        )

        if better_value:
            pieces = new_pieces
            total_same, total_different = new_total_same, new_total_different
        elif same_value:
            pieces = new_pieces
        elif temperature > 0:
            probability = math.exp(-1/temperature)
            if select_with_probability(probability):
                pieces = new_pieces
                total_same, total_different = new_total_same, new_total_different
        else:
            raise ValueError

        new_percentage = (100 - rate) / 100
        temperature *= new_percentage

    return pieces


# Tests
if __name__ == '__main__':
    # print('Test for read_input()')
    piece_groups = read_input()
    # print(piece_groups)

    # print('Test for pick_random_location()')
    # for i in range(10):
    #     print(pick_random_location())

    # print('Test for is_overlapping()')
    # print(is_overlapping([('', '', 3, 2), ('', '', 5, 4)], (2, 3)))
    # print(is_overlapping([('', '', 3, 2), ('', '', 5, 4)], (5, 4)))

    # print('Test for pick_free_location(), initialize_board(), and draw_board()')
    # print('Use 64 pieces input to test pick_free_location()')
    pieces = initialize_board(piece_groups)
    print(pieces)
    # print(draw_board(pieces))

    # print('Test for format_piece()')
    # piece = random.choice(pieces)
    # print(*format_piece(piece))

    # print('Test for is_inside_board()')
    # print(is_inside_board(-1, -1))
    # print(is_inside_board(0, 0))
    # print(is_inside_board(7, 7))
    # print(is_inside_board(8, 8))

    # print('Test for find_piece_at()')
    # piece = find_piece_at(pieces, *pick_random_location())
    # if piece:
    #     print(*format_piece(piece))
    # else:
    #     print(piece)

    # print('Test for count_pieces_attacked_by()')
    # piece = random.choice(pieces)
    # color, piece_type, row, col = piece
    # while piece_type != 'queen': # change piece_type as needed
    #     piece = random.choice(pieces)
    #     color, piece_type, row, col = piece
    # print(*format_piece(piece))
    # print(*count_pieces_attacked_by(pieces, piece))

    # print('Test for count_all_attacks()')
    # for piece in pieces:
    #     counts = count_pieces_attacked_by(pieces, piece)
    #     print(*format_piece(piece), counts)
    # print(count_all_attacks(pieces))

    # print('Test for hill_climbing()')
    # print(draw_board(pieces))
    # print(*count_all_attacks(pieces))
    # new_pieces = hill_climbing(pieces)
    # print(draw_board(new_pieces))
    # print(*count_all_attacks(new_pieces))

    # print('Test for simulated_annealing()')
    # print(draw_board(pieces))
    # print(*count_all_attacks(pieces))
    # new_pieces = simulated_annealing(
    #     pieces, 1000, 1, 10
    # )
    # print(draw_board(new_pieces))
    # print(*count_all_attacks(new_pieces))