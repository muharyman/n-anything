import os

from annealing_interface import annealing_interface

# import hill_climbing, simulated_annealing, genetic_algorithm

dummy = """
Success!
(This is a dummy message)"""

welcome = """
Welcome to Orenji N-ything Solver!
Select mode:
- Standard Mode (type 'standard')
- Quick Solve: Hill Climbing (type 'quickhc')
- Quick Solve: Simulated Annealing (type 'quicksa')
- Quick Solve: Genetic Algorithm (type 'quickga')
For help, type 'help' or '?'
To quit, press Ctrl-C"""

help_message = """
Type the solving mode command to start solving.

Modes:
- Standard Mode (recommended)
Command: standard
Description: Step-by-step procedure to solve the problem

- Quick Solve: Hill Climbing
Command: quickhc
Description: Solve 'input.txt' with Hill Climbing algorithm

- Quick Solve: Simulated Annealing
Command: quicksa
Description: Solve 'input.txt' with Simulated Annealing algorithm

- Quick Solve: Genetic Algorithm
Command: quickga
Description: Solve 'input.txt' with Genetic algorithm"""

algorithm_selection = """
Standard Mode
Select the algorithm to solve the problem:
- Hill Climbing ('hc')
- Simulated Annealing ('sa')
- Genetic Algorithm ('ga')"""

filename_input = """
Type the filename for input:"""

customize_parameter = """
Do you want to customize the algorithm parameter? ('y'/'n')"""

max_steps = """
Maximum number of steps:"""

starting_temperature = """
Starting temperature:"""

descent_rate = """
Descent rate:"""

population_size = """
Population size:"""

mutation_chance = """
Mutation chance:"""

file_error = """
There is no such file in the current directory"""

wrong = """
Wrong input! Better luck next time"""

help_variations = ['help', '?']
yes_variations = ['y', 'yes']
no_variations = ['n', 'no']

algorithms = ['hc', 'sa', 'ga']

def prompt(message):
    """Print the message, prompt for user input, then process it."""
    print(message)
    user_input = input('\n> ')
    cleaned_input = user_input.strip().lower()

    return cleaned_input

def main():
    mode = prompt(welcome)
    if mode == 'standard':
        algorithm = prompt(algorithm_selection)
        if algorithm not in algorithms:
            print(wrong)
            return

        filename = prompt(filename_input)
        if not os.path.isfile(filename):
            print(file_error)
            return

        customize = prompt(customize_parameter)

        if customize in yes_variations:
            steps = prompt(max_steps)
            if algorithm == 'hc':
                print(dummy)

            elif algorithm == 'sa':
                temperature = prompt(starting_temperature)
                rate = prompt(descent_rate)
                annealing_interface(filename, steps, temperature, rate)

            elif algorithm == 'ga':
                size = prompt(population_size)
                chance = prompt(mutation_chance)
                print(dummy)

        elif customize in no_variations:
            if algorithm == 'hc':
                print(dummy)

            elif algorithm == 'sa':
                annealing_interface()

            elif algorithm == 'ga':
                print(dummy)

        else:
            print(wrong)

    elif mode == 'quickhc':
        print(dummy)

    elif mode == 'quicksa':
        annealing_interface()

    elif mode == 'quickga':
        print(dummy)

    elif mode in help_variations:
        print(help_message)

    else:
        print(wrong)

# Main Program
if __name__ == '__main__':
    main()