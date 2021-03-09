import argparse

from generator.utility import extractor, file_util
from generator import bingo_generator

# Parsing Args
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--textfile", help="A newline-delimited txt file with values for Bingo squares. If none is provided, random integers from 0-75 will be used. These are not consistent with the normal numbering conventions of Bingo.")
parser.add_argument("-c", "--cards", help="The number of cards to create.")

args = parser.parse_args()

if args.textfile:
    source_value_file = args.textfile
    print("Using {} to extract Bingo square content".format(source_value_file))
else:
    source_value_file = None
    print("Using numbers 0 to 75 as Bingo square content")

if args.cards:
    num_cards = args.cards
else:
    num_cards = 20
print("Creating {} bingo cards".format(num_cards))

# Clear out old output directory
file_util.clear_and_create_output_dir()

# Get bingo values
values = extractor.extract_values(source_value_file)

# Run the script
bingo_generator.create_bingo_cards(values, num_cards)