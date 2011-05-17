# -*- coding: utf-8 -*-
from ToolBox import *
from kasiski_long import all_differences

# def pertinence(crible, periode):
#     n = len(crible)
#     crible = crible.upper()
#     occ = []
#     ret = {}
#     # ret est un dictionnaire dont les clés sont les lettres qui composent le crible. 
#     # Il n'y a qu'une seule occurence de ces clés
#     # A chaque clé est associé un tuple informant sur le nombre d'occurences de cette clé 
#     # dans le mot et ses positions
#     # exemple : {'c':[4, [1,3,5], p]} : 
#     #           La lettre c apparait 4 fois dans le crible au position [1,3,5]
#     #           p est l'indice de pertinence de la lettre


#     for i,c in enumerate(crible):
#         if c in ret:
#             # la clé existe deja
#             ret[c][0] += 1        # on rajoute +1 au nb d'occurence de la lettre
#             indices = list(ret[c][1])
#             tmp = i
#             for ii in indices:
#                 if tmp - ii == periode:
#                     ret[c][2] += 1
#                 tmp = ii
                                                
#             ret[c][1].append(i)   # on enregistre sa position

#         else:
#             ret[c]=[1,[i], 0]        


    
#     return ret

def pertinence(crible,periode):
    l = all_differences(crible)
    indice = 0
    for e in l:
        if e % periode == 0:
            indice += 1
    return float(indice)/float((len(l)))
    #return float(indice)/(float(len(crible))/float(periode))

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
    raw_input()


    # RARETE
    print "EVALUATION DE LA RARETE"
    for n,d in FREQ_TABLE_DICT.items():
        print n,d[0]
    choix=int(raw_input('Veuillez choisir la langue:'))
    while not isinstance(crible,int) and (choix < 0 or choix > len(FREQ_TABLE_DICT)):
        print choix + " n'est pas un choix valide!"
        choix=int(raw_input('Veuillez choisir la langue:'))
        
    freq_table = FREQ_TABLE_DICT.get(choix)[1]
    
    print "Evaluation de la rarete du crible \""+crible+"\"..."
    rar = rarete(freq_table,crible)
    print "resultat:"+str(rar)
    print "--------------------"


 
if __name__ == "__main__":
    main()
