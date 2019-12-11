import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('string', type=str)
    parser.add_argument('file', type=str)
    parser.add_argument('number' , type=int)

    return parser.parse_args()

def find_string(file, string):
    file1 = open(file, 'r')
    if string in file1.read():
        print(True)
    else:
        print(False)


def print_line(file, string):
    file1 = open(file, "r")
    for line in file1:
        if re.match(string, line):
            print(line)


args = parse_args()

if args.number == 1:
    find_string(args.file, args.string)
elif args.number == 2:
    print_line(args.file, args.string)
