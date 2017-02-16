from itertools import permutations

def main(string, other_string):
    perms = set(''.join(p) for p in permutations(string))
    return(other_string in perms)