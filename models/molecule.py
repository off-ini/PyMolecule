
class Molecule:
    def __init__(self, name, formule):
        self.name = name # Nom de la molecule 
        self.formule = formule # Formule moleculaire
        self.atomes = list() # Liste des atomes, leurs masse et leurs index (nombre) dans la molecule 

    # Calcule de masse basé sur la liste des atomes - return float : masse
    def calcMasse(self):
        rlt = 0
        for item in self.atomes:
            rlt += int(item.nombre) * float(item.masse)
            print('\t- {} * {} = {}'.format(int(item.nombre), float(item.masse), rlt))
        return round(rlt, 1)

    
    # Traduire la formule de la molecule dans un code intermediere
    """
    Exemple 
    1- K2Cr2O7 
        'k 2 Cr 2 O 7'
    2- H2O
        'H 2 O'
    3- CO2
        'C 1 0 2'
    4- CH4
        'C 1 H 4'
    """
    # L'objectif c'est de split sur ce code intermédiere les traduire en Atome
    def parseFormule(self):
        state = 0 # 0 init - 1 uppacase - 2 lowercase - 3 number
        rlt = ""
        for l in self.formule:
            try:
                number = int(l)
            except: number = ""

            if type(number) is int: # Si un nombre

                if state == 0 or state == 3:
                    rlt += l
                elif state == 1 or state == 2:
                    rlt += " {}".format(l)
                state = 3

            elif type(l) is str: # Si un caratere
                if l.isupper():

                    if state == 0:
                        rlt += l
                    elif state == 1 or state == 2:
                        rlt += " 1 {}".format(l)
                    elif state == 3:
                        rlt += " {}".format(l)
                    state = 1

                elif l.islower():
                    if state == 0 or state == 1 or state == 3:
                        rlt += l
                    state = 2
        return rlt