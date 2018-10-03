import math
import random
from random import randint 
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

# Mengembalikan inisiasi awal sebanyak x gen
def initPieces(x) :
    gen = []
    for i in range(0, x) :
        piece_groups = read_input()
        pieces = initialize_board(piece_groups)
        gen.append(pieces)
    
    return gen

def calcFitness (gen) :
    fitnessVal = []
    for piece in gen :
        fitnessVal.append(count_all_attacks(piece))

    return fitnessVal

def sortGen (gen, fitnessVal) :
    newFitnessVal = []
    newGen = []
    tempFitnessVal = []
    tempGen = []
    j = len(fitnessVal)
    for idx in range(0,j) :
        idx_min = 0
        val_min = fitnessVal[0][0]
        for i in range(0, len(fitnessVal)) :
            if (val_min > fitnessVal[i][0]) :
                val_min = fitnessVal[i][0]
                idx_min = i
        tempFitnessVal.append(fitnessVal[idx_min])
        tempGen.append(gen[idx_min])
        gen.pop(idx_min)
        fitnessVal.pop(idx_min)
    
    for idx in range(0,j) :
        idx_max = 0
        valLeftMax = tempFitnessVal[0][0]
        val_max = tempFitnessVal[0][1]
        for i in range(0, len(tempFitnessVal)) :
            if (valLeftMax == tempFitnessVal[i][0]) :
                if (val_max < tempFitnessVal[i][1]) :
                    val_max = tempFitnessVal[i][1]
                    idx_max = i
            else :
                break
        newFitnessVal.append(tempFitnessVal[idx_max])
        newGen.append(tempGen[idx_max])
        tempGen.pop(idx_max)
        tempFitnessVal.pop(idx_max)
    
    new = newGen, newFitnessVal
    return new

def genetic (gen,x) :
    new_gen = []
    idx_max = int(len(gen)*9/10)
    for i in range (0,idx_max) :
        new_gen.append(gen[i])

    maxx = gen[0]
    for aa in range (0,x) :
        new_gens = []
       
        for temp_gen in gen :
            child1 = []
            child2 = []

            #Selection
            idx_border = randint(1,(len(temp_gen)-1))
            
            num_choose = randint(0,(len(new_gen)-1))

            for i in range (0,idx_border) :
                child1.append(temp_gen[i])
                child2.append(new_gen[num_choose][i])

            for i in range (idx_border,len(temp_gen)) :
                child1.append(new_gen[num_choose][i])
                child2.append(temp_gen[i])

            if (count_all_attacks(child1)[0] > count_all_attacks(child2)[0]) :
                new_gens.append(child2)
                temp = child2
            elif (count_all_attacks(child1)[0] < count_all_attacks(child2)[0]) :
                new_gens.append(child1)
                temp = child1
            else :
                if (count_all_attacks(child1)[1] < count_all_attacks(child2)[1]) :
                    new_gens.append(child2)
                    temp = child2
                else :
                    temp = child1
                    new_gens.append(child1)

            if (count_all_attacks(maxx)[0] > count_all_attacks(temp)[0]) :
                maxx = temp
            elif (count_all_attacks(maxx)[0] == count_all_attacks(temp)[0]) :
                if (count_all_attacks(maxx)[1] < count_all_attacks(temp)[1]) :
                    maxx = temp
                
            """
            if (count_all_attacks(child1)[0] > count_all_attacks(temp_gen)[0]) :
                new_gens.append(temp_gen)
            elif (count_all_attacks(child1)[0] < count_all_attacks(temp_gen)[0]) :
                new_gens.append(child1)
            else :
                if (count_all_attacks(child1)[1] < count_all_attacks(temp_gen)[1]) :
                    new_gens.append(temp_gen)
                else :
                    new_gens.append(child1)

            if (count_all_attacks(child2)[0] > count_all_attacks(new_gen)[0]) :
                new_gens.append(new_gen)
            elif (count_all_attacks(child2)[0] < count_all_attacks(new_gen)[0]) :
                new_gens.append(child2)
            else :
                if (count_all_attacks(child2)[1] < count_all_attacks(new_gen)[1]) :
                    new_gens.append(new_gen)
                else :
                    new_gens.append(child2)
            """


            #serang_sama1,serang_beda1 = count_all_attacks(child1)
            #serang_sama2,serang_beda2 = count_all_attacks(child2)



            """
            #Mutation
            child1[randint(0,len(child1))] = randint(0,len(child1))
            idx_mut = randint(0,len(child1))
            """
            #print(draw_board(child1))
            #print(draw_board(child2))

            #print("\nGenerasi "+ str(count) + " : " + str(serang_sama1) + " " + str(serang_beda1))
            #print("Generasi "+ str(count) + " : " + str(serang_sama2) + " " + str(serang_beda1) + "\n")       

        gen_temp = []
        for i in range(0,len(gen)) :
            gen_temp.append(new_gens[i])
        
        gen = sortGen(gen_temp, calcFitness(gen_temp))[0]

    print(draw_board(maxx))
    print(*count_all_attacks(maxx))

gen = initPieces(100)
print(gen[0])
fitness = calcFitness(gen)
sortbro = sortGen(gen,fitness)
genetic(sortbro[0],1000)