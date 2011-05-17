# -*- coding: utf-8 -*-
from ToolBox import *

# Nom:      kasiski_court
# Obj:      Permet de trouver la période par la méthode "courte"
#           Trouve toute les sous chaines répétées de longueur 'l' dans 'text'
# Param:    le texte chiffré, la taille de la sous chaine
def kasiski_court(text, l):
    lst = []
    for i in range(len(text)-l):
        target = text[i:i+l]
        found = text[i+l:].find(target)
        if found != -1:
            f = found+i+l
            if i>0 and text[i-1:i+l] == text[f-1:f+l]:
                continue
            if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
                continue            
            print "%-10s %3d" % (target, found+l)
            lst.append(found+l)
    return lst


def ktest(text):
    ctext = ""
    for c in text:
        c = c.upper()
        if c in ALPHABET:
            ctext += c;

    distances = []
    for l in range(len(text)/2,2,-1):
        print "test d'une longueur de sous chaine de:"+str(l)
        distances.extend(kasiski_court(ctext, l))
    if len(distances) < 2:
        raise BaseException('Impossible de trouver la période avec qu\'une seule distance')
    print ''
    print "determination de la période: pgcd de "+str(distances)+" ="
    return distances


if __name__ == "__main__":
    def main():
        while True:
            text = raw_input ("text? ")
            if len(text) == 0:
                break

            print pgcdn(ktest(text))

    main()
