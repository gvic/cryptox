#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Vigenere with alphabets

Usage : vigenere_alphabets -d/-e <file_text> <file_alphabets>
"""
from __future__ import with_statement

import sys
import getopt


alphabet0 = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
alphabet1 = "efghijklmnopqrstuvxyzabcd".upper()
alphabet2 = "defghijklmnopqrstuvxyzabc".upper()
alphabet3 = "cdefghijklmnopqrstuvxyzab".upper()
alphabet4 = "fghijklmnopqrstuvxyzabcde".upper()
alphabet5 = "bcdefghijklmnopqrstuvxyza".upper()
alphabet6 = "defghijklmnopqrstuvxyzabc".upper()

base = len(alphabet0)

alphabets = [alphabet0, alphabet1, alphabet2, alphabet3, alphabet4, alphabet5, alphabet6]

chiffre = "phyjs lyddq fdzxg asgzz qqehx gkfnd rxuju giocy tdxvk sbxhh "
chiffre += "uypoh dvyry mhuhp uydkj oxphe tozsl etnpm vffov pdpaj xhyyn " 
chiffre += "ojygg aymeq ynfuq lnmvl yfgsu zmqiz tlbqg yugsq eubvn rcred "
chiffre += "gruzb lrmxy uhqhp zdrrg crohe pqxuf ivvrp lphon thvdd qfhqs "
chiffre += "ntzhh hnfep mqkyu uexkt ogzgk yuumf vijdq dpzjq sykrp lxhxq "
chiffre += "rymvk lohhh otozv dkspp suvjh d"

text = "LEVER ITABL EAUTE URDUV OLDES DIAMA NTSET DELAS SASSI NATDE SSOLD ATSQU IESCO RTAIE NTLEC ONVOI COMMI SDANS LANUI TDUVI NGTDE UXJAN VIERM ILHUI TCENT VINGT SIXNE STDON CPASJ OAMDA COSTA INJUS TEMEN TCOND AMNEA MORTC ESTMO ILEMI SERAB LEEMP LOYED ELADM INIST RATIO NDUDI STRIC TDIAM ANTIN OUIMO ISEUL QUISI GNEDE MONVR AINOM ORTEG A"


def encrypt(ptext, alph):    
    ctext = ""
    pos = 0
    for c in ptext:
        c = c.upper()
        alphabet = alph[pos+1]
        if not c in alph[0]:
            ctext += c
        else:
            a = alph[0].find(c)
            c = alphabet[a]
            ctext += c
            pos = (pos+1) % (len(alph)-1)
    return ctext

    
def decrypt(ptext, alph):        
    ctext = ""
    pos = 0
    for c in ptext:
        c = c.upper()
        alphabet = alph[pos+1]
        if not c in alph[0]:
            ctext += c
        else:
            a = alphabet.find(c)
            ctext += alph[0][a]
            pos = (pos+1) % (len(alph)-1)
    return ctext

def process_text(file_in):
    text = ""
    with open(file_in) as f:
        for line in f:
            text += line.upper()
    return text

def process_alphabets(file_in):
    alphabets = []
    with open(file_in) as f:
        for line in f:
            alphabets.append(line.upper())
    return alphabets

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hed", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        DECRYPT = None
        # Process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                return 0
            elif o in ("-d"):
                DECRYPT = True
            elif o in ("-e"):
                DECRYPT = False

        # If DECRYPT is set we need to arguments
        if not DECRYPT is None:
            if len(args)!=2:
                raise Usage("Not enough arguments")
            else:
                text = process_text(args[0])
                alphabets = process_alphabets(args[1])
                if DECRYPT:
                    print decrypt(text, alphabets)
                else:
                    print encrypt(text, alphabets)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
