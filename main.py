import stuct
import argparse

from spec import dmpspec

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
    description='Converts a DefleMask DMP instrument file to ...other stuff.')
parser.add_argument('input', help='the input file name')
#parser.add_argument('output', help='the output file name')
args = parser.parse_args()

# read instrument file
dmp = open(args.input, "rb").read()
