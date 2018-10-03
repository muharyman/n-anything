import board

board_size = 8
files = 'abcdefgh'
ranks = '12345678'

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