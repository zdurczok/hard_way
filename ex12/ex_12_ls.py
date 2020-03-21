import os, argparse

# simple implementation of bash ls command with options -a, -c and -S

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('path', type=str)
    parser.add_argument('option', type=str)

    return parser.parse_args()

# ls -a

def show_all(path):
    return os.listdir(path)

# ls -c

def by_change_time(path):
    os.chdir(path)
    return sorted(os.listdir(path), key=os.path.getmtime)
# ls -S

def by_size(path):
    os.chdir(path)
    return sorted(os.listdir(path), key=os.path.getsize)

args = parse_args()

if args.option == 'a':
    print(show_all(args.path))
elif args.option == 'c':
    print(by_change_time(args.path))
elif args.option == 'S':
    print(by_size(args.path))
