# -*- coding: utf-8 -*-

from ToolBox import *

# 
def pertinence(crible, periode):
   
    return ret

def rarete(freq_table ,crible):
    """
    Nom:   rarete
    Param: 
      - table de frequence du langage naturel : dictionnaire
      - crible : string
    Desc: 
      Cette fonction renvoie une valeur entre 0 et 1 pour caractérisé 
      la rareté du crible.
      1 décrit une rareté maximale.
    """

    n = len(crible)
    # On récupere la lettre qui a la plus haute frequence ds le dictionnaire
    max_freq = max(freq_table.values())
    tot = 0
    for c in crible.upper():
        tot += freq_table.get(c)

    return abs((1 - tot/(n*max_freq)))

def vraisemblance():
    return ret


# Test Function
def main():

    # PERTINENCE
    print "RECHERCE DE LA PERTINENCE"
    crible=input('Veuillez tapez un crible:')
    while ~isinstance(crible,str):
        print crible + " n'est pas une chaine de caractère!"
        crible=input('Veuillez tapez un crible:')

    period=input('Veuillez tapez une période:')
    while ~isinstance(period,int):
        print crible + " n'est pas un entier!"
        crible=input('Veuillez tapez une period:')

    print "Calcul de la pertinence..."
    per = pertinence(crible,period)
    print "resultat:"+str(per)
    print "--------------------"
    
 
if __name__ == "__main__":
    main()