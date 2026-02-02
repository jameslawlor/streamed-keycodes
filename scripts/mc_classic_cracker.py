"""
Monte Carlo cracker for ClassicKeypad
"""

from streamed_keycodes.keypads.classic import ClassicKeypad
import matplotlib.pyplot as plt
import time

N_SIMULATIONS = 10000  # Number of simulations to run
N_ITER = 20 # Number of iterations per simulation
NKEYS = 4
NDIGITS = 10
CHECK_MOD = 1000 # How often to print progress


if __name__ == "__main__":
    start_time = time.time()

    avg_attempts_all = []

    for _sim in range(N_SIMULATIONS):
        keypad = ClassicKeypad(nkeys=NKEYS, ndigits=NDIGITS)
        guesses = keypad.generate_list_of_guesses()
        y = []

        for _ in range(N_ITER):
            attempts = 0

            for guess in guesses:
                attempts += 1
                if keypad.check_solution(guess):
                    keypad.solution = keypad.generate_solution()
                    break

            y.append(attempts)

        elapsed_time = time.time() - start_time
        avg_attempts = sum(y) / N_ITER
        avg_attempts_all.append(avg_attempts)
        if (_sim + 1) % CHECK_MOD == 0:
            print(f"Simulation {_sim + 1}/{N_SIMULATIONS} complete. Elapsed time: {elapsed_time:.2f} seconds.")

    print("Expectation value of attempts to crack ClassicKeypad:", sum(avg_attempts_all) / N_SIMULATIONS)
    plt.hist(avg_attempts_all, bins=30, edgecolor='black')
    plt.title(f"Histogram of Average Attempts to Crack ClassicKeypad\n(NKEYS={NKEYS}, NDIGITS={NDIGITS}, N_ITER={N_ITER}, N_SIMULATIONS={N_SIMULATIONS})")
    plt.xlabel("Average Number of Attempts")
    plt.ylabel("Frequency")
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('classic-keypad-histogram.png', dpi=100, bbox_inches='tight')
    plt.close()