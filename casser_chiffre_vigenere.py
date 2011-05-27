#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kaboom the given crypted(with vigenere method) text

Usage : casser_chiffre_vigenere (-l LANG) <file_in>
Options :
   -l LANG : Choose language entered text ("FRANCAIS", "ENGLISH")
"""
from __future__ import with_statement
from analyse_freq import *
from kasiski_long import *
from ToolBox import *

import sys
import getopt


# Casser le chiffre a l'aide de L'Indice de Coincidence Mutelle
# Fonctionne pour des vigeneres simples
def casser(chiffre, periode, Lang_Freq):
    # bloc decomposition
    blocs = [""]*periode
    newblocs = [""]*periode
    deltas = [0]*(periode-1)
    
    i = 0
    for c in chiffre:
        if c.upper() in ALPHABET:
            blocs[i] += c
            i = (i+1) % periode

    # calcul de l'ICM de bloc[0] a chacun des 26 decalages de bloc[j]
    for j in range(periode-1):
        ICMS = {}
        for i,v in enumerate(ALPHABET):
            ICMS[i] = ICM(blocs[0], shift(blocs[j+1], -i))

        alist = sorted(ICMS.iteritems(), key=lambda (k,v): (v,k))
        # max des ICMs -> Delta entre bloc[0] et bloc[j]
        deltas[j], icm = alist[len(ALPHABET)-1]

    # print deltas

    # Recherche exhaustive de k0
    # Attention a la reference en faisant newblocs = blocs..
    newblocs = list(blocs)
    for i,v in enumerate(ALPHABET):
        newblocs[0] = shift(blocs[0],i)
        for j in range(periode-1):
            newblocs[j+1] = shift(blocs[j+1],i-deltas[j])

        # Rebuild process
        k = 0
        j = 0
        text = ""
        for c in chiffre:
            if c.upper() in ALPHABET:
                text += newblocs[k][j/periode]
                k = (k+1) % periode
                j += 1
            else:
                text += c

        # Compare the most frequent letter of the text result
        # to the most frequent of the language
        Chaine_Freq = Freq_Calc(Nbr_Letters(text))
        A = sorted(Chaine_Freq.keys())
        B = sorted(Lang_Freq.keys())

        x = max(Chaine_Freq.values())
        y = max(Lang_Freq.values())
        for ii in A:
            if Chaine_Freq[ii] == x:
                L_a = ii
                break
        for jj in B:
            if Lang_Freq[jj] == y:
                L_b = jj
                break

        if L_a == L_b:
            if i == 0:
                key = ALPHABET[0]
            else:
                key = ALPHABET[26-i]

            for d in deltas:
                pos = d-i
                if pos<0:
                    pos = 26+pos
                key += ALPHABET[pos]

            # Print possible key and text
            print "Cle : %s" % key
            print "Text : %s" % text            
        

# Nombre d'occurence d'un caractere c dans une chaine x
def nbre_occurence(c, x):
    tot = 0

    chaine = x.upper()
    c = c.upper()
    i = chaine.find(c)
    while  i >= 0:
        tot += 1
        chaine = chaine[(i+1):]
        i = chaine.find(c)


    return tot

# Indice de Coincidence Mutuelle
def ICM(x,y):
    tot = float(0)
    l1 = len(x)
    l2 = len(y)

    for l in ALPHABET:
        tot += nbre_occurence(l,x)*nbre_occurence(l,y)

    tot = float(tot)/(l1*l2)

    return tot

def process_text(file_in):
    text = ""
    with open(file_in,'r') as f:
        for line in f:
            text += line.upper()
    f.close()
    return text


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hl:", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        LANG = None
        # Process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                return 0
            elif o in ("-l"):
                LANG = a

        # C mon!
        if len(args)!=1: #and not LANG is None:
            raise Usage("Not enough arguments")
        else:
            chiffre = process_text(args[0])
            if LANG == "FRANCAIS":
                langue = FRENCH_PROB
            elif LANG == "ENGLISH":
                langue = ENGLISH_PROB
            else: # Default choice
                langue = FRENCH_PROB
                
                
            prompt = "A"
            while not prompt.upper() == "Q":
                casser(chiffre, kasiski_long(chiffre), langue)
                prompt = raw_input("Quit or try again? (Q) or (A)")

            
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
