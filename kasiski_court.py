from ToolBox import *

# Nom:      kasiski_court
# Obj:      Permet de trouver la période par la méthode "courte"
# Param:    le texte chiffré, la taille de la sous chaine
def kasiski_court(text, l):
    """
    Find all repeated substrings of length 'l' in 'text'
    """
    for i in range(len(text)-l):
        target = text[i:i+l]
        found = text[i+l:].find(target)
        if found != -1:
            # if the match can be extended in either direction, don't
            # report it
            f = found+i+l
            if i>0 and text[i-1:i+l] == text[f-1:f+l]:
                continue
            if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
                continue            
            print "%-10s %3d %s" % (target, found+l, str(factor(found+l)))

def ktest(text):
    """
    Strip all characters that are not in the cipher alphabet.
    
    Report all substrings from longest to shortest.  The longest
    possible substring is half the ciphertext length.  Substrings
    shorter than 5 are not reported.
    """
    ctext = ""
    for c in text:
        c = c.upper()
        if c in ALPHABET:
            ctext += c;

    for l in range(len(text)/2,2,-1):
        kasiski_court(ctext, l)


if __name__ == "__main__":
    def main():
        while True:
            text = raw_input ("text? ")
            if len(text) == 0:
                break
            ktest(text)

    main()
