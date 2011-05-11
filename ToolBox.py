"""
Librairie rassemblant des fonctions utiles pour la cryptographie
"""


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ENGLISH_PROB = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02360,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
    }


def cshift(str,n):
    slen=len(str)
    return str[n:slen+1]+str[0:n]

def factor (n):
    """
    Return a list of [factor, exponet] pairs for the prime factors
    of parameter n.
    """

    ret = []

    fact = 2                # possible factor
    while fact*fact <= n:
        power = 0           # power for the factor
        
        while n % fact == 0:    # '%' is the modulus (remainder) operator
            power = power + 1
            n = n / fact

        if power != 0:
            ret += [(fact, power)]
        
        fact = fact + 1

    # if n has not been reduced to 1, it is the last factor and has
    # not been printed
    if n != 1:
        ret += [(n, 1)]

    return ret
