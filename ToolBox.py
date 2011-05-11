"""
Librairie rassemblant des fonctions utiles pour la cryptographie
"""


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
