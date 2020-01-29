from collections import Counter

# simple implementation of bash uniq command using Counter

# case sensitive duplicates uniq -d (printing all as lowecase)

def only_duplicates(filename):
    with open(filename) as f:
        c = Counter(c.strip() for c in f if c.strip())
        for line in c:
            if c[line] > 1:
                print(line)

# case insensitive unique lines uniq -i (printing all as lowercase)

def ignore_case(filename):
    with open(filename) as f:
        c = Counter(c.strip().lower() for c in f if c.strip())
        for line in c:
            if c[line] == 1:
                print(line)

# print only unique lines uniq -u

def only_uniq(filename):
    with open(filename) as f:
        c = Counter(c.strip() for c in f if c.strip())
        for line in c:
            if c[line] == 1:
                print(line)

# compare n-first characters, print unique lines

def n_characters(filename, n):
    with open(filename) as f:
        f = [line.strip()[:n] for line in f]
        c = Counter(c.strip() for c in f if c.strip())
        for line in c:
            if c[line] == 1:
                print(line)
