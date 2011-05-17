# -*- coding: utf-8 -*-

def Nbr_Letters(Chaine):
    Tab_Letters = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,
'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    for Letter in Tab_Letters:
        for Char in Chaine:
            if Char.upper()==Letter:
                Tab_Letters[Letter]+=1
    return Tab_Letters
 
def Freq_Calc(Tab_Nbr_Letters):
    Total_Occurence = 0
    for i in Tab_Nbr_Letters:
        Total_Occurence += Tab_Nbr_Letters[i]
    for Indice in Tab_Nbr_Letters:
        if Tab_Nbr_Letters[Indice] != 0.:
            Tab_Nbr_Letters[Indice]=100./(Total_Occurence/Tab_Nbr_Letters[Indice])
    return Tab_Nbr_Letters
 
def Freq_Analyse(Chaine_Freq, Lang_Freq):
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
    i = 0
    I_a, I_b =0,0
    while i < len(A):
        if A[i] == L_a:
            I_a = i
        elif B[i] == L_b:
            I_b = i
        i+=1
    return I_b-I_a,{L_a:L_b}

