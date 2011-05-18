# -*- coding: utf-8 -*-
from ToolBox import *
from kasiski_long import all_differences
import operator


def pertinence(crible,periode):
    l = all_differences(crible)
    indice = 0
    for e in l:
        if e % periode == 0:
            indice += 1
    if len(l) >0:
        return float(indice)/float((len(l)))
    else:
        return 0
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


def frequence_crible(crible):
    d = {}
    for c in crible:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)

def table_frequences(chiffre,periode):
    table = [{}]*(periode)
    for i,c in enumerate(chiffre):
        ii = i % periode
        print table
        print ii, table[ii]
        raw_input()
        if c in table[ii]:
            table[ii][c] += 1
        else:
            table[ii][c] = 1
    return table

def vraisemblance():

    return ret


# Test Function
def main():
    
    print ''
    print 'Veuillez choisir la fonction a évaluer:'
    print '(P)ertinence'
    print '(R)areté'
    print '(L)es deux'
    print '(Q)uitter'
    question=str(raw_input())

    if question == 'Q':
        return 4
    while not isinstance(question,str) or (question != 'P' and question != 'L' and question != 'R'):
        print question + " n'est pas valide!"
        question=str(raw_input())


    if question == "P" or question == "L":
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

    if question == "R" or question == "L":
        # RARETE
        if question == "R":
            crible=str(raw_input('Veuillez tapez un crible:'))
            while not isinstance(crible,str):
                print crible + " n'est pas une chaine de caractère!"
                crible=str(raw_input('Veuillez tapez un crible:'))
            
        print "EVALUATION DE LA RARETE"
        for n,d in FREQ_TABLE_DICT.items():
            print n,d[0]
        choix=int(raw_input('Veuillez choisir la langue:'))
        while not isinstance(choix,int) and (choix < 0 or choix > len(FREQ_TABLE_DICT)):
            print choix + " n'est pas un choix valide!"
            choix=int(raw_input('Veuillez choisir la langue:'))
        
        freq_table = FREQ_TABLE_DICT.get(choix)[1]
        
        print "Evaluation de la rarete du crible \""+crible+"\"..."
        rar = rarete(freq_table,crible)
        print "resultat:"+str(rar)
        print "--------------------"


 
if __name__ == "__main__":
    ret = 0
    while ret != 4:
        ret = main()


