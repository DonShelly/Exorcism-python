"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
LAYER_PREP_TIME = 2

# general estimated bake time
EXPECTED_BAKE_TIME = 40



def bake_time_remaining(elapsed_bake_time: int = 0):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_layers: int = 1):
    """return the time the las needs to be prepared

    Takes layers and calculated total time
    """
    return LAYER_PREP_TIME * num_layers


def elapsed_time_in_minutes(num_layers, elapsed_bake_time):

    """Returns elapsed time in miniutes

    tales num layters and elapsed bake and sums them using a function call to preparation_time_in_minutes
    """
    return elapsed_bake_time + preparation_time_in_minutes(num_layers)
