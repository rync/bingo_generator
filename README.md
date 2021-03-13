# bingo_generator
Python script for generating random bingo cards for parties and showers and acts of subversive hooliganism.

## Getting Started

After cloning this repo, two things are required to get up and running:
1. Install python dependencies using `pip install -r requirements.txt`
2. Run `sudo apt install wkhtmltopdf`. This can be done on a Linux distro, and maybe something similar can be done Mac with brew, but this is untest. I'm unsure what will happen on Windows at the moment.

I also recommend install Jupyter Notebook to access the notebook under `./notebook`.

## Running the Script

You can run the script using `./run.py main.py`, and by default, it will generate 20 cards with 75 randomly allotted numbers.

Unfortunately, the script does not yet generate 'proper' bingo cards following normal convention (this is slated for future work), but you can insert your own file using the `-t` flag. This will take each line in a txt file and use the resultant list as the values to select from for randomly generated bingo cards.

## Output

The script will create an output directory that includes an individual png file for each bingo card.
