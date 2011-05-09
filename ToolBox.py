

# Classe qui rassemble des fonctions utilitaires
class ToolBox:

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def cshift(str,n):
        slen=len(str)
        return str[n:slen+1]+str[0:n]

    def factor (n):
        """
        print the prime factors of parameter n.
        """
    
        factorPrinted = False   # true after the first factor is printed

        fact = 2                # possible factor
        while fact*fact <= n:
            power = 0           # power for the factor
        
            while n % fact == 0:    # '%' is the modulus (remainder) operator
                power = power + 1
                n = n / fact

            if power != 0:
                if factorPrinted:
                    print "*",
                if power > 1:
                    print "%d^%d" % (fact, power),
                else:
                    print fact,
                factorPrinted = True
        
            fact = fact + 1

        # if n has not been reduced to 1, it is the last factor and has
        # not been printed
        if n != 1:
            if factorPrinted:
                print "*",
            print n
        else:
            # the factors were printed without newline; print it now
            print





    def findsubs(text, l):
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
                print "%-10s %3d %s" % (target, found+l, str(self.factor(found+l)))
            

