import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', type=str)
    parser.add_argument('option', type=str)

    return parser.parse_args()



def simple_sort(filename):
    with open(filename) as lines:
        print(''.join(sorted(lines)), end="")

def reversed_sort(filename):
    with open(filename) as lines:
        print(''.join(sorted(lines, reverse=True)), end="")

def l_blanks_sort(filename):
    with open(filename) as lines:
        print(''.join(sorted(lines, key=lambda x:x.replace(' ',''))), end="")

def numbers_sort(filename):
    with open(filename) as lines:
        print(''.join(sorted(lines,  key=lambda s: re.sub('[-+]?[0-9]+', '', s))), end="")

def case_sort(filename):
    with open(filename) as lines:
        print(''.join(sorted(lines, key=str.casefold)), end="")

args = parse_args()

if args.option == '-':
    print(simple_sort(args.filename))
elif args.option == 'b':
    print(l_blanks_sort(args.filename))
elif args.option == 'r':
    print(reversed_sort(args.filename))
elif args.option == 'd':
    print(numbers_sort(args.filename))
elif args.option == 'f':
    print(case_sort(args.filename))
