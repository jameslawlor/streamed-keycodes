import random
from abc import ABC, abstractmethod

class Keypad(ABC):
    def __init__(self, nkeys=None, ndigits=None, solution=None):
        self.nkeys = nkeys
        self.ndigits = ndigits

        if not solution:
            self.solution = self.generate_solution()
        else:
            verified_solution = self.check_input_solution_is_valid(solution)
            self.solution = verified_solution

    def check_input_solution_is_valid(self, user_input_solution):
        if len(user_input_solution) != self.nkeys:
            raise ValueError(f"Input solution must have exactly {self.nkeys} digits.")
        for digit in user_input_solution:
            if not (0 <= digit < self.ndigits):
                raise ValueError(f"Each digit must be between 0 and {self.ndigits - 1}.")

    def generate_solution(self):
        return tuple(random.randint(0, self.ndigits - 1) for _ in range(self.nkeys))

    def check_solution(self, attempt):
        return attempt == self.solution

    def __repr__(self):
        args = ', '.join(f'{k}={v!r}' for k, v in vars(self).items())
        return f"{self.__class__.__name__}({args})"
    
    @abstractmethod
    def generate_list_of_guesses(self):
        pass
