# implementation of bash cut command - ex 8 LMPTHW by Zed A. Shaw

import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('string', type=str)
    parser.add_argument('file', type=str)
    parser.add_argument('number' , type=int)

    return parser.parse_args()

# bash cut -c / a)specific
# b) to/from c) range

def print_characters(file, string):
    with open(file, 'r') as f:
        if len(string) == 1:
            for line in f:
                print(line[int(string)])
        elif len(string) == 2:
            if string[0] == '-':
                for line in f:
                    print(line[:int(string[1])])
            elif string[0] != '-':
                for line in f:
                    print(line[int(string[0]):])
        elif len(string) == 3:
            for line in f:
                print(line[int(string[0]):int(string[2])])

# bash cut -f ( spaces included)

def return_from_field(file, string):
    with open(file, 'r') as f:
        for line in f:
            line = line.split(' ')
            if int(string) < len(line):
                print(line[int(string)])
            else:
                print("Index number  has excluded len of this line")

# bash cut -s

def lines_with_delimeter(file, string):
    with open(file, 'r') as f:
        for line in f:
            if string in line:
                print(line)
            else:
                print("Delimeter not in this line")

args = parse_args()

if args.number == 1:
    print_characters(args.file, args.string)
elif args.number == 2:
    return_from_field(args.file, args.string)
elif args.number == 3:
    lines_with_delimeter(args.file, args.string)
