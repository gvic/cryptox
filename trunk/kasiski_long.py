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

    all_differences = determin_list(all_differences)
    print all_differences
    ret = max(all_differences)

    # The max isn't always the solution..
    # Let's try to finds the maxS
    # By getting a max limit = max - 5%*max
    limit = ret-ret/20  
    maxs = [i for i in all_differences if i>limit]
    solutions = [indexP(all_differences,v) for v in maxs]
    # Solutions should be sorted (as we read the list from beginning to end)
    
    

    return min(solutions)

#Small useful function
def indexP(lst,v):
    return lst.index(v)+1

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


def determin_list(input_liste):
    l = range(24)
    lst = [0 for e in l]
    
    # On parcourt de 0 a 23
    for i in l:
        # on parcourt la liste des distances
        for j in input_liste: 
            if j % (i+1) == 0:
                lst[i] += 1;
                               
    return [(e+1)*ee for e,ee in zip(l,lst)]


# Just to test
def main():
    # the main code goes here
    
    # lanaki test text
    # expected result : 7
    text1 = "RNQJH  AUKGV  WGIVO  BBSEJ  CRYUS  FMQLP  OFTLC"
    text1 += "MRHKB BUTNA  WXZQS  NFWLM  OHYOF  VMKTV  HKVPK"
    text1 += "KSWEI  TGSRB LNAGJ  BFLAM  EAEJW  WVGZG  SVLBK"
    text1 += "IXHGT  JKYUC  HLKTU MWWK"
    
    # project test text
    # expected result : 6 or 12
    text = "phyjs  lyddq fdzxg asgzz qqehx gkfnd rxuju giocy tdxvk sbxhh"
    text += "uypoh  dvyry mhuhp uydkj oxphe tozsl etnpm vffov pdpaj xhyyn" 
    text += "ojygg  aymeq ynfuq lnmvl yfgsu zmqiz tlbqg yugsq eubvn rcred"
    text += "gruzb  lrmxy uhqhp zdrrg crohe pqxuf ivvrp lphon thvdd qfhqs"
    text += "ntzhh  hnfep mqkyu uexkt ogzgk yuumf vijdq dpzjq sykrp lxhxq"
    text += "rymvk  lohhh otozv dkspp suvjh d"
      
    print "indice:"
    print kasiski_long(text)
    print"¦-¦-¦-¦-¦-¦-¦-¦"
 
if __name__ == "__main__":
    main()
