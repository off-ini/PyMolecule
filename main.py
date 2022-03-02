from models import *

# Structre des 50 premier Atomes
atome_list = [
    ('H',1),
    ('He', 4),
    ('Li', 6.941),
    ('Be', 9.0122),
    ('B', 10.811),
    ('C', 12.0107),
    ('N', 14.0067),
    ('O', 15.9994),
    ('F', 18.9984),
    ('Ne', 20.1797),
    ('Na', 22.9897),
    ('Mg', 24.305),
    ('Al', 26.9815),
    ('Si', 28.0855),
    ('P', 30.9738),
    ('S', 32.065),
    ('Cl', 35.453),
    ('K', 39.0983),
    ('Ar', 39.948),
    ('Ca', 40.078),
    ('Sc', 44.9559),
    ('Ti', 47.867),
    ('V', 50.9415),
    ('Cr', 51.9961),
    ('Mn', 54.938),
    ('Fe', 55.845),
    ('Ni', 58.6934),
    ('Co', 58.9332),
    ('Cu', 63.546),
    ('Zn', 65.39),
    ('Ga', 69.723),
    ('Ge', 72.64),
    ('As', 74.9216),
    ('Se', 78.96),
    ('Br', 79.904),
    ('Kr', 83.8),
    ('Rb', 85.4678),
    ('Sr', 87.62),
    ('Y', 88.9059),
    ('Zr', 91.224),
    ('Nb', 92.9064),
    ('Mo', 95.94),
    ('Tc', 98),
    ('Ru', 101.07),
    ('Rh', 102.9055),
    ('Pd', 106.42),
    ('Ag', 107.8682),
    ('Cd', 112.411),
    ('In', 114.818),
    ('Sn', 118.71)
]

# Ecrire le fichier files/Atomes.txt
def remplireAtome():
    with open('files/Atomes.txt', 'w') as file:
        atomes = ""
        i = 0
        for a in atome_list:
            if len(atome_list) - 1 == i:
                atomes += "{} {}".format(a[0], a[1])
            else : atomes += "{} {}\n".format(a[0], a[1])
            i += 1
        file.write(atomes)

# Lire le fichier files/Atomes.txt return - List<Atome>
def lireAtome():
    remplireAtome()
    atomes = list()
    with open('files/Atomes.txt', 'r') as data:
        Lines = data.readlines()
        for line in Lines:
            lineTable = line.split(" ")
            atomes.append(Atome(lineTable[0].strip(), lineTable[1].strip()))
    return atomes

# Verifie si un symbole appartien a la liste des atomes - return Atome()
def checkAtome(symbole, atomes):
    for item in atomes:
        if item.symbole == symbole:
            return item
    return None

# Lire le fichier files/Molecules.txt renvoie la liste des molecules  - return List<Molecule>
def lireMolecules():
    atomes = lireAtome()
    molecules = list()
    with open("files/Molecules.txt", 'r') as data:
    #with open("files/M", 'r') as data:
        Lines = data.readlines()
        for line in Lines:

            lineTable = line.strip().split("*")
            molecule = Molecule(lineTable[0], lineTable[1])
            codeTable = molecule.parseFormule().split(' ') # Recupérer le code de la molecule et split sur scpace

            for i in range(0, len(codeTable), 2): # Parcourir avec un pas de 2 pour recupérer les Symboles
                item = checkAtome(codeTable[i], atomes)
                if item != None:
                    try:
                      a = Atome(item.symbole, item.masse, codeTable[i+1]) # i+1 pour ecupérer les index ou nombre
                    except:
                        a = Atome(item.symbole, item.masse, 1) # A la fin du tableau si on a pas un nombre ajouter 1
                    molecule.atomes.append(a)

            molecules.append(molecule)

    return molecules

# Récupere la liste de molecules List<Molecule> , Calcule et remplie le fichier outputs/Resultats.txt
def masseAtome():

    with open("outputs/Resultats.txt", 'w') as file:
        molecules = lireMolecules()
        rlt = ""
        i = 0
        for item in molecules:
            if len(atome_list) - 1 == i:
                rlt += "{} {}".format(item.name, item.calcMasse())
            else:
                rlt += "{} {}\n".format(item.name, item.calcMasse())
            i += 1
            print('\t\t|')
        file.write(rlt)

# Point d'entrer du programe
if __name__ == '__main__':
    print("\t--- Start ---")
    masseAtome() # Calcule de la masse moleculaire
    print("\t--- Finish ---")