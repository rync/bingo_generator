import numpy as np

def extract_values(filename, numbers=75):
    # Extracts values from a text file,
    #  assuming each unique value is on a new line.
    # If filename is None, will generate a random list of numbers.
    if filename:
        with open(filename) as f:
            values = f.read().splitlines()
    else:
        values = np.arange(0, numbers)
    return values