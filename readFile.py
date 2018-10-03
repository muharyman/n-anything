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