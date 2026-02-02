from itertools import product
import random

from streamed_keycodes.keypads.base import Keypad

class Streampad(Keypad):
    def __init__(self, nkeys=4, ndigits=10, solution=None):
        super().__init__(nkeys, ndigits, solution)

    def generate_list_of_guesses(self):
        pass