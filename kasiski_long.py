# -*- coding: utf-8 -*-
from ToolBox import *

# Nom:      kasiski_long
# Obj:      Permet de trouver la periode par la méthode "longue"
# Param:    le texte chiffre
def kasiski_long(text):

    # Remove all none alphabet chars
    ctext = ""
    for c in text:
        c = c.upper()
        if c in ALPHABET:
            ctext += c

    all_differences = []
    for poss in letter_positions(ctext):
        all_differences.extend(differences(poss))

    return all_differences

# Function which return a list of lists containing the positions of each letters
# in the given text
def letter_positions(text):
    # Letters position
    positions = [[] for i in range(26)]
    pos = 0
    # For each characters of the text
    for char in text:
        char = char.upper()
        # If char is a letter of the alphabet
        l = ALPHABET.find(char)
        if l>=0:
            # Save the position in the appropriate list
            positions[l].append(pos)
        pos = pos+1
    return positions
            
# Returns all the possible differences between the elmts of a given list
def differences(lst):
    res = []

    lst.sort()
    llst = lst
    for e in lst:
        llst = llst[1:]
        res.extend([j-e for j in llst])

    return res


# Just to test
def main():
    # the main code goes here
    print kasiski_long("abc db cab")
 
if __name__ == "__main__":
    main()
