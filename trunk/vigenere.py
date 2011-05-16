"""
Vigenere
"""

alphabet0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabet1 = "gqkreshtovwmcjxyzpflundiab".upper()
# alphabet2 = "mvqwjxoyszlrhpundtkiabcdfg".upper()
# alphabet3 = "cmgoapeqjrshiftvwkbxyzlund".upper()
# alphabet4 = "jsotgvkwqxypfmzlurhndiabce".upper()
# alphabet5 = "vnydsiwalbczrxefguthjkmopq".upper()
# alphabet6 = "hrmsftjvpwxoekyzlqgundiabc".upper()
# alphabet7 = "wdzitaxbucelsyfghnvjkmopqr".upper()

base = len(alphabet0)

# alphabets = [alphabet1, alphabet2, alphabet3, alphabet4, alphabet5, alphabet6, alphabet7]
alphabets = [alphabet0]
nalphabets = len(alphabets)

def encrypt(ptext, key):
    k = ""
    for c in key:
        c = c.upper()
        if c in alphabet0:
            k += c
    
    ctext = ""
    i = 0
    pos = 0
    for c in ptext:
        c = c.upper()
        alphabet = alphabets[pos]
        pos = (pos+1) % nalphabets
        if not c in alphabet:
            ctext += c
        else:
            a = alphabet.find(c)
            b = alphabet.find(k[i])
            c = alphabet[(a+b) % base]
            ctext += c
            i = (i+1) % len(k)
    return ctext


def decrypt(ptext, key):    
    k = ""
    for c in key:
        c = c.upper()
        if c in alphabet0:
            k += c
    
    ctext = ""
    i = 0
    pos = 0
    for c in ptext:
        c = c.upper()
        alphabet = alphabets[pos]
        pos = (pos+1) % nalphabets
        if not c in alphabet:
            ctext += c
        else:
            a = alphabet.find(c)
            b = alphabet.find(k[i])
            ctext += alphabet[(a-b) % base]
            i = (i+1) % len(k)
    return ctext


def main():
    decode = raw_input ("(E)ncrypt or (D)ecrypt? ")
    if decode[0].upper() == "D":
        decode = True
    else:
        decode = False
    kw = raw_input ("Enter keyword: ")
    if kw != "":
        keyword = kw
    tx = raw_input ("Text: ")
    if tx != "":
        text = tx
    if kw!="" and tx!="":
        if decode:
            print decrypt (text, keyword)
        else:
            print encrypt (text, keyword)


if (__name__ == "__main__"):
    main()    
