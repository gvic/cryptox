# -*- coding: utf-8 -*-

from analyse_freq import *
from kasiski_long import *
from ToolBox import *

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
        for i in A:
            if Chaine_Freq[i] == x:
                L_a = i
                break
        for j in B:
            if Lang_Freq[j] == y:
                L_b = j
                break

        if L_a == L_b:
            print text
            prompt = raw_input("Does it look ok? (Y) or (N)")
            # Stop FOR loop if it's ok!
            if prompt.upper() == "Y":
                break
            
        

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

def main():

    chiffre = "LP BWA SPNA RSE LI PHZSM QU XOVQE WA UVEFX XNREAOéR ; CLR KUANUV CEYSM RN êERM FI MIMA PZUZIU, BUM PEFX UêZE BUQ FOYT TRS ALCF DTFNVCTLMF à CZNBRNEEZ RN EOCGE LUBEE NHWFE Y’OVG PZIVG CZUBHMP D’MA DéDIZRR ALCF QF’ITF EY OVG. EY QCBI TL V’RSE PIF VCAQFEXBTNBWE YHE EOCF SP TZBMAEVG : MLIA CLFTôB PEWA BéZOTGVR QFE TN PFIAFAYCM QE MIMA JFGME EE DQFTTNOHEC LM IRLI L’NVPC TR FLUF, DUT EAG PCOXEEXEVG CP QC’BN YOUZE WE JBN DEVF OF LI EATSWA, EDT VNTFRMYLPMMAT éRATR EY TWHS WEA UOXMMF ; EE AQAST QCR LL DQIECSQGé DP NWF OAIVVOYS VR VTEVG PLS LR CP QCR LPS CAS DOVG PWUA EATSWANLBTRS BUM YED ACGRPS, UNID SMHLPMMAT OE KR QFE VBUD CWADFIABND NWF PPNAéRS AAZ QIGEZFED VWVED, EB AE NOVFIOéRWAS AAA YED MêURS NHWFED. CIE CP N’MFT AAA NSDEH Q’AGOQE L’PSXEIE BWA, MLIA YE ARQACTPIY EDT LR L’LPXYIBUME BTEV. YED PTHS RRIADPS âURS DOVG CLPIOLPS LRS ALCF GCAVQS GIKRS LUAFI MIMA QFE LRS ALCF GCAVQED VMETFS ; MG CPUF DUT NM ZACCPRNE QCR FZRB YEYTMZEYT XRUGEVG AGAVPEC BMNUNOCC DLVIATLGM, F’IWS AHIGEVG TZURBUCS TR DCOQG CSEUVN, BUM AE QOVG CPUF DUT CWHRPNB RT BUQ F’EY éLWVGYEVG."    
    chiffre = "PHXJS LXDDQ FDYWG ZSGYY QQEHW GKFND RWUJU GIOCX TDWVK SBWHH UXPOH DVXRX MHUHP UXDKJ OWPHE TOYSL ETNPM VFFOV PDPZJ WHXXN OJXGG ZYMEQ XNFUQ LNMVL XFGSU YMQIY TLBQG XUGSQ EUBVN RCRED GRUYB LRMWX UHQHP YDRRG CROHE PQWUF IVVRP LPHON THVDD QFHQS NTZHH HNFEP MQKXU UEWKT OGYGK XUUMF VIJDQ DPYJQ SXKRP LWHWQ RXMVK LOHHH OTOYV DKSPP SUVJH D"

    casser(chiffre, kasiski_long(chiffre), FRENCH_PROB)

#    casser("Phyjslyddqfdzxgasgzzqqehxgkfndrxujugiocytdxvksbxhhuypohdvyrymhuhpuydkjoxphetozsletnpmvffovpdpajxhyynojyggaymeqynfuqlnmvlyfgsuzmqiztlbqgyugsqeubvnrcredgruzblrmxyuhqhpzdrrgcrohepqxufivvrplphonthvddqfhqsntzhhhnfepmqkyuuexktogzgkyuumfvijdqdpzjqsykrplxhxqrymvklohhhotozvdksppsuvjhd", 6, FRENCH_PROB)

#    casser("PHXJS LXDDQ FDYWG ZSGYY QQEHW GKFND RWUJU GIOCX TDWVK SBWHH UXPOH DVXRX MHUHP UXDKJ OWPHE TOYSL ETNPM VFFOV PDPZJ WHXXN OJXGG ZYMEQ XNFUQ LNMVL XFGSU YMQIY TLBQG XUGSQ EUBVN RCRED GRUYB LRMWX UHQHP YDRRG CROHE PQWUF IVVRP LPHON THVDD QFHQS NTZHH HNFEP MQKXU UEWKT OGYGK XUUMF VIJDQ DPYJQ SXKRP LWHWQ RXMVK LOHHH OTOYV DKSPP SUVJH D", 6)

    # s = ["bonjour", "monsieur"]
    # l = s 
    # print s
    # print s[0]
    # l[0] = shift(s[0],1)
    # print s[0]

if (__name__ == "__main__"):
    main()    
