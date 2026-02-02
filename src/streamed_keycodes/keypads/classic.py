from itertools import product
import random

from streamed_keycodes.keypads.base import Keypad

class ClassicKeypad(Keypad):
    def __init__(self, nkeys=4, ndigits=10, solution=None):
        super().__init__(nkeys, ndigits, solution)

    def generate_list_of_guesses(self):
        """
        Create a randomly-shuffled list of all possible guesses for the classic keypad.
        """
        all_combinations = list(product(range(self.ndigits), repeat=self.nkeys))
        random.shuffle(all_combinations)
        return all_combinations