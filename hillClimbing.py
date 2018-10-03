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