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

    ad = all_differences(ctext)

    ad = determin_list(ad)
    ret = max(ad)

    # The max isn't always the solution..
    # Let's try to finds the maxS
    # By getting a max limit = max - 10%*max
    limit = ret-ret/20  
    maxs = [i for i in ad if i>limit]

    solutions = [indexP(ad,v) for v in maxs]
    # Solutions should be sorted (as we read the list from beginning to end)
    length = len(solutions)-1
    if length > 0:
        print "Here are the period values possible:"
        print solutions
        print "Which one do you wan't to choose? (0,1,..,%d)" % length

        x = -1
        while x<0:
            try:
                x = int(raw_input())
                if x > len(solutions)-1:
                    x = -1
                    raise ValueError
            except ValueError:
                print 'Invalid Number'
    elif length <0:
        raise Exception
    else:
        x = 0

    return solutions[x]

#Small useful function
def indexP(lst,v):
    return lst.index(v)+1

# Get all differences between the letters of a text
def all_differences(text):
    diffs = []
    for poss in letter_positions(text):
        diffs.extend(differences(poss))
    return diffs


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
    l = range(48)
    lst = [0 for e in l]
    
    # On parcourt de 0 a 23
    for i in l:
        # on parcourt la liste des distances
        for j in input_liste: 
            if j % (i+1) == 0:
                lst[i] += 1;
                               
    return [(e+1)*ee for e,ee in zip(l,lst)]


# Test Function
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
      
    print kasiski_long(text)
 

if __name__ == "__main__":
    main()
