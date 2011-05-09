

# Classe qui rassemble des fonctions utilitaires
class ToolBox:

    def cshift(str,n):
        slen=len(str)
        return str[n:slen+1]+str[0:n]

