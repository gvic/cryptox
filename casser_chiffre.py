# -*- coding: utf-8 -*-

from analyse_freq import *
from ToolBox import *

def casser(chiffre, periode, lang_freq):
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
            ICMS[i] = ICM(blocs[0], shift(blocs[j+1], i))
    
        alist = sorted(ICMS.iteritems(), key=lambda (k,v): (v,k))
        print alist
        # max des ICMs -> Delta entre bloc[0] et bloc[j]
        deltas[j], icm = alist[len(ALPHABET)-1]
        print deltas

    # Recherche exhaustive de k0
    newblocs = blocs
    for i,v in enumerate(ALPHABET):
        print i
        print blocs[0]
        newblocs[0] = shift(blocs[0],i)
        print newblocs[0]
        for j in range(periode-1):
            newblocs[j+1] = shift(blocs[j+1],deltas[j]-i)

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

        print text
        raw_input("Tapez une touche pour continuer.")
        

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
#    casser("WY ORV DYAV MDN YD KSIFH LF GBQLP FN PQPOK SICNNJéM ; NUE FPLWHQ XPHFH MY êNEH AT VVHV AIHUDF, KHH KPOK PêUP KHL AZHG OMD JYXA OCSIQNCYHA à NIAWMYNRU MY NBXBP UHWZP WURAP H’BQB AIVQB NIHWCXY Q’HV OéMVUMC JYXA BO’VOA PH BQB. PH DXWT CY Q’MDN CDA GLNLAPGOOIMFR TCP NBXA DY GUWXJRQB : XUVV XWOGôW KPFN WéUZCTQM BOR OI AOVVALHPH LP VVHV UOTHZ PN QLAECAJCPL YH DCUV G’IGYP OM QUHA, YFC RVB ALBSZPGRQB NY DX’WY HBPUP FR EWY MRQA ZO YD ZLCFRV, PMG QIEOEHTWYZHVE éANOM PH GRCD FRV PZGZHA ; PN NLVDC DXM WU QLDPLFLBé OY ARA ZJVQQZHF QM GCRQB AUF GM NY DXM WYF XVD MBQB AFHV ZLCFRVYUOOMD KHH TPM NXBCYF, PITM FHCWYZHVE XR FM BOR QWFM PRVOOVVWYM ARA AYAVéMD JNU LTPRUAPM IRQPM, RW VP WBQATXéERVD JNV TPM ZêPMD WURAPM. PDZ NY A’HAE JNV IDMRC L’LPBLZ W’YFSZTN ORV, XUVV TP JELVNCCDT PMG GM W’UCSTTKHHZ MCRQ. TPM COCD AEDVOYF âPMD MBQB NUCDJWYF GMD JYXA RLNQLD PVFMD UHVAT VVHV BOR GMD JYXA RLNQLPM IHZEOF ; HB NYHA YFC AH ULLPKMYN DXM QIEW TPHGHUPHG SMFPRQB LPNQKPL OHIFWBXX OUIDVEUTH, A’TFF VCTPRQB EIHMWFLF OM OLBLB NBRPQY, KHH VP ZBQB NYHA YFC PRCCYAW ME KHL A’PH éYRQRHRQB.", 5, FRENCH_PROB)

    s = ["bonjour", "monsieur"]
    print s
    print s[0]
    shift(s[0],1)
    print s[0]

if (__name__ == "__main__"):
    main()    
