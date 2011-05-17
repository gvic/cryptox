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
    crible=str(raw_input('Veuillez tapez un crible:'))
    while not isinstance(crible,str):
        print crible + " n'est pas une chaine de caractère!"
        crible=str(raw_input('Veuillez tapez un crible:'))

    period=int(raw_input('Veuillez tapez une période:'))
    while not isinstance(period,int):
        print str(period) + " n'est pas un entier!"
        crible=int(raw_input('Veuillez tapez une période:'))

    print "Calcul de la pertinence..."
    per = pertinence(crible,period)
    print "resultat:"+str(per)
    print "--------------------"
    


    # RARETE
    print "EVALUATION DE LA RARETE"
    print FREQ_TABLE_DICT
    for n,d in FREQ_TABLE_DICT.items():
        print n,d[0]
    choix=int(raw_input('Veuillez choisir la langue:'))
    while not isinstance(crible,int) and (choix < 0 or choix > len(FREQ_TABLE_DICT)):
        print choix + " n'est pas un choix valide!"
        choix=int(raw_input('Veuillez choisir la langue:'))
        
    freq_table = FREQ_TABLE_DICT.get(choix)[1]

    print "Evaluation de la rarete du crible \""+crible+"\"..."
    rar = rarete(freq_tabl,crible)
    print "resultat:"+str(rar)
    print "--------------------"


 
if __name__ == "__main__":
    main()
