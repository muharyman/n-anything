import random
import math

def select_with_probability(probability):
    """Within the specified probability, returns True."""
    return random.random() < probability

def format_piece(piece):
    """Returns a tuple with a (color, type, rank, file) format."""
    color, piece_type, row, col = piece
    return color, piece_type, files[col], ranks[row]