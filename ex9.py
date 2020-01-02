import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', type=str)
    parser.add_argument('re_exp', type=str)
    parser.add_argument('option', type=str)

    return parser.parse_args()

def strings_with_re(file, re_exp, option):
    with open(file, 'r') as f:
        if option == 'findall':
            for line in f:
                if re.findall(re_exp, line):
                    print(line)
        elif option == 'split':
            for line in f:
                print(re.split(re_exp, line))
        elif option == 'sub':
            print("Please use function string_sub(file, str_old, str_new)"
                  "providing file, a string to be replaced and a new string or"
                  "an old pattern together with a new pattern.")
        elif option == 'search':
            for line in f:
                if re.search(re_exp, line):
                    print("Pattern found inside the string")
                else:
                    print("Pattern not found")
        elif option == 'group':
            for line in f:
                if re.search(re_exp, line):
                    match = re.search(re_exp, line)
                    print(match.group())
                else:
                    print("Pattern not found")

args = parse_args()

print(strings_with_re(args.file, args.re_exp, args.option))
