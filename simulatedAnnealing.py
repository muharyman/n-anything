import random
import math
from board import initialize_board
from board import draw_board
from readFile import read_input
from attackCount import count_all_attacks
from board import pick_free_location
from probability import select_with_probability

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