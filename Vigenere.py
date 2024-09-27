"""
TODO (je te le fait pas en bas parce que je sais pas vraiment où ça va enft)

En gros, quand tu passes les tests, au lieu de te marquer "caractere special intraitable,
il affiche rien et skip direct à la fin

C est pas facile a expliquer, lance juste le programme et prends l option 3 ou 4, tu verras
"""

from time import sleep

def VigenereMenu():

    EntreeUtilisateur : str
    Clef : str
    Chiffrement : bool

    print("Chiffrement de Vigenere")
    print("1. Chiffrer quelque chose")
    print("2. Déchiffrer quelque chose")
    print("3. Afficher des tests de chiffrement")
    print("4. Afficher des tests de déchiffrement")
    print("5. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        EntreeUtilisateur = input("Entrez le mot à chiffrer: ")
        Clef = input("Entrez la clé de chiffrement: ")
        PrepareMot(EntreeUtilisateur, Clef, True)
    elif choice == "2":
        EntreeUtilisateur = input("Entrez le mot à déchiffrer: ")
        Clef = input("Entrez la clé de déchiffrement: ")
        PrepareMot(EntreeUtilisateur, Clef, False)
    elif choice == "3":
        ChiffrementVigenereTests()
    elif choice == "4":
        DechiffrementVigenereTests()
    elif choice == "5":
        return
    else:
        print("Choix invalide")
        VigenereMenu()

def PrepareMot(Mot, Clef, Chiffrement):

    #Initialisation des variables

    codeAlphabet: int
    carASCII: int
    inverseur: bool
    motAtraiter : str
    strResultat: str

    motVerif: [int]
    lstTemporaire: [int]
    cleVerif: [int]

    cleVerif = []
    motVerif = []
    lstTemporaire = []

    inverseur = True

    # Code

    for _ in range(2): # Pour traiter le mot, puis la clé
        if inverseur:
            motAtraiter = Mot # On traite le mot
        else:
            motAtraiter = Clef # On traite la clé

        # Parcours du mot à chiffrer
        for car in motAtraiter:
            carASCII = ord(car)
            if not ((65 <= carASCII <= 90) or (97 <= carASCII <= 122)): # Test : Si caractère n'est pas entre a-z ou A-Z

                #  On vérifie si car spécial
                if 192 <= carASCII <= 197: # A majuscule
                    lstTemporaire.append(65)
                elif 200 <= carASCII <= 203: # E majuscule
                    lstTemporaire.append(69)
                elif 204 <= carASCII <= 207: # I majuscule
                    lstTemporaire.append(73)
                elif 210 <= carASCII <= 214: # O majuscule
                    lstTemporaire.append(79)
                elif 217 <= carASCII <= 220: # U majuscule
                    lstTemporaire.append(85)
                elif 221 == carASCII: # Y majuscule
                    lstTemporaire.append(89)


                elif 224 <= carASCII <= 229: # a minuscule
                    lstTemporaire.append(97)
                elif 232 <= carASCII <= 235: # e minuscule
                    lstTemporaire.append(101)
                elif 236 <= carASCII <= 239: # i minuscule
                    lstTemporaire.append(105)
                elif 242 <= carASCII <= 246: # o minuscule
                    lstTemporaire.append(111)
                elif 249 <= carASCII <= 252: # u minuscule
                    lstTemporaire.append(117)
                elif 253 == carASCII or 255 == carASCII: # y minuscule
                    lstTemporaire.append(121)

                else : # Caractère spécial intraitable
                    return 'Caractère spécial intraitable'

            else:
                lstTemporaire.append(carASCII)

        if inverseur:
            motVerif = lstTemporaire.copy()
            lstTemporaire.clear()
            inverseur = False
        else:
            cleVerif = lstTemporaire.copy()

    if Chiffrement:
        print ((ChiffrementVigenere(motVerif, cleVerif)))
    else:
        print ((DechiffrementVigenere(motVerif, cleVerif)))
    sleep(2)
    VigenereMenu()

def ChiffrementVigenere(motAchiffrer : [int], clef : [int]) -> str:
    """Chiffre un mot en utilisant le chiffrement de Vigenère
    Préconditions: motAchiffrer est un mot en majuscules et/ou minuscules
    Postconditions: retourne le mot chiffré"""

    # Initialisation des variables
    carCle: int
    facteur1: int
    facteur2: int
    i: int
    code: int

    lstInt: [str]
    lstStr: [str]

    lstInt = []
    lstStr = []


    # Chiffrement
    for i in range(len(motAchiffrer)):  # On chiffre le mot
        carCle = clef[i % len(clef)] # Pour éviter les erreurs de dépassement

        if 65 <= motAchiffrer[i] <= 90: # On vérifie si la lettre du mot est en majuscule
            facteur1 = 65

        elif 97 <= motAchiffrer[i] <= 122: # On vérifie si la lettre du mot est en minuscule
            facteur1 = 97

        if 65 <= carCle <= 90: # On vérifie si la lettre de la clé est en majuscule
            facteur2 = 65

        elif 97 <= carCle <= 122: # On vérifie si la lettre de la clé est en minuscule
            facteur2 = 97

        code = (motAchiffrer[i] - facteur1 + carCle - facteur2) % 26 + facteur1
        lstInt.append(code)

    for code in lstInt:  # On convertit les chiffres en lettres
        lstStr.append(chr(code))

    strResultat = ''.join(lstStr)  # On concatène les lettres

    return strResultat

def DechiffrementVigenere(motADechiffrer : [int], clef : [int]) -> str:
    """
    Dechiffre un mot en utilisant le chiffrement de Vigenère
    Préconditions: motADechiffrer est un mot en majuscules et/ou minuscules
    Postconditions: retourne le mot déchiffré
    """

    #Initialisation des variables
    carCle:int
    i: int
    code: int
    facteur1: int
    facteur2: int

    lstInt: [str]
    lstStr: [str]

    # Initialisation
    lstInt = []
    lstStr = []

    # Dechiffrement

    for i in range(len(motADechiffrer)):  # On chiffre le mot
        carCle = clef[i % len(clef)] # Pour éviter les erreurs de dépassement

        if 65 <= motADechiffrer[i] <= 90: # On vérifie si la lettre du mot est en majuscule
            facteur1 = 65

        elif 97 <= motADechiffrer[i] <= 122: # On vérifie si la lettre du mot est en minuscule
            facteur1 = 97

        if 65 <= carCle <= 90: # On vérifie si la lettre de la clé est en majuscule
            facteur2 = 65

        elif 97 <= carCle <= 122: # On vérifie si la lettre de la clé est en minuscule
            facteur2 = 97

        code = ((motADechiffrer[i] - facteur1) - (carCle - facteur2)) % 26 + facteur1
        lstInt.append(code)

    for code in lstInt:  # On convertit les chiffres en lettres
        lstStr.append(chr(code))

    strResultat = ''.join(lstStr)  # On concatène les lettres

    return strResultat



def ChiffrementVigenereTests():
    # Tests
    motsTest = ["Texteclair", "TexTECLaiR", "Téxtècläîr", "Texteclair!"]
    clefsTest = ["Clef", "Cléf", "ClEf", "Clef!"]
    i = 0

    for mot in motsTest:
        print("")
        for clef in clefsTest:
            i += 1
            print("Test n°", i, " : ", PrepareMot(mot, clef, True))

    VigenereMenu()

def DechiffrementVigenereTests():
    # Tests
    motsTest = ["Vpbygnpfkc", "VpbYGNPfkC", "Vpbygnpfkc", "Vpbygnpfkc!"]
    clefsTest = ["Clef", "Cléf", "ClEf", "Clef!"]
    i = 0

    for mot in motsTest:
        print("")
        for clef in clefsTest:
            i += 1
            print("Test n°", i, " : ", PrepareMot(mot, clef, False))

    VigenereMenu()

VigenereMenu()