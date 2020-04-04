import os

# simple implementation of bash tail command, which is working only in a given directory

N = int(input("Please provide a number of last lines to be printed: "))
filenames = list(input("Please provide comma separated filenames with their extensions: ").split())

def print_last_lines(filenames, N):
    for filename in filenames:
        lines = [line.rstrip() for line in open(filename)][-N:]
        print('*** ', filename, ' ***')
        for line in lines:
            print(line)
