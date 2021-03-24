import hw1_help as hw1


def naive_with_rc(p,t):
    frwd = hw1.naive(p,t)
    rev = hw1.naive(reverseComplement(p),t)
    matches = frwd + rev
    matches = list(set(matches))
    return matches
