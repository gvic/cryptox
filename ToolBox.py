# -*- coding: utf-8 -*-
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

FRENCH_PROB = {
    'A' : 0.083944,
    'B' : 0.007669,
    'C' : 0.033297,
    'D' : 0.040699, 
    'E' : 0.145037,  
    'F' : 0.012109,  
    'G' : 0.009495,  
    'H' : 0.007973,  
    'I' : 0.081828,  
    'J' : 0.006377,  
    'K' : 0.000638,  
    'L' : 0.058405,  
    'M' : 0.029355,  
    'N' : 0.075570,  
    'O' : 0.053669,  
    'P' : 0.032087,  
    'Q' : 0.012613,  
    'R' : 0.070209,  
    'S' : 0.080091,  
    'T' : 0.074775,  
    'U' : 0.059808,  
    'V' : 0.015791,  
    'W' : 0.000067,  
    'X' : 0.004098,  
    'Y' : 0.003155,  
    'Z' : 0.001240
    }

FREQ_TABLE_DICT = {
    1:('ENGLISH',ENGLISH_PROB),
    2:('FRANCAIS',FRENCH_PROB)
}


def cshift(str,n):
    slen=len(str)
    return str[n:slen+1]+str[0:n]

# Decalage de chaque lettre de n
def shift(strg,n):
    shift2 = lambda txt,sft=1:''.join([[ch,chr((ord(ch) - ord(['A','a'][ch.islower()]) + sft)%26+ord(['A','a'][ch.islower()]))][ch.isalpha()] for ch in txt])

    return shift2(strg,n)


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

def pgcd(a,b):
    """
    pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre 
    les 2 nombres entiers a et b
    """
    while b<>0:
        a,b=b,a%b
    return a
        
def pgcdn(n):
    """
    Calcul du 'Plus Grand Commun Diviseur' de n valeurs entières (Euclide)
    """
    p = pgcd(n[0], n[1])
    for x in n[2:]:
        p = pgcd(p, x)
    return p

def distance_letters(a,b):
    """
    # Compute the diffs between two letters
    # input : two letters
    #
    # Example : distence_letters("a","c") returns 2
    """
    pos_a = ALPHABET.find(a.upper())
    pos_b = ALPHABET.find(b.upper())

    if pos_b == -1 or pos_a == -1:
        raise BaseException("Char %s and %s not recognized.." % a,b)
    else:
        diff = pos_b - pos_a

    # Special case..
    if a.upper()=='Z' and b.upper()=='A' or a.upper()=='A' and b.upper()=='Z':
        diff = 1;
        
    return abs(diff)
    
def swap(string, i, j):
    l = len(string)
    if i<0 or j<0 or i>l or j>l:
        raise BaseException('The String is too small, change swap parameters')
    else:
        lstring = list(string)
        #swap
        lstring[i-1],lstring[j-1] = lstring[j-1],lstring[i-1]

    return ''.join(lstring)
