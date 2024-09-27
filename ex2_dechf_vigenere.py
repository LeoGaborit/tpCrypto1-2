def dechiffrementVigenere(motADechiffrer : str, clef : str) -> str:
    """
    Dechiffre un mot en utilisant le chiffrement de Vigenère
    Préconditions: motADechiffrer est un mot en majuscules et/ou minuscules
    Postconditions: retourne le mot déchiffré
    """

    #Initialisation des variables
    codeAlphabet: int
    carASCII: int
    i: int
    code: int

    facteur1: int
    facteur2: int

    inverseur: bool

    motAtraiter : str

    lstTemporaire: [int]
    motDechiffre: [int]
    cleDechiffre: [int]
    lstInt: [str]
    lstStr: [str]
    strResultat: str

    # Initialisation
    lstTemporaire = []
    motDechiffre = []
    cleDechiffre = []
    lstInt = []
    lstStr = []

    inverseur = True

    for _ in range(2):  # Pour traiter le mot, puis la clé
        if inverseur:
            motAtraiter = motADechiffrer  # On traite le mot
        else:
            motAtraiter = clef  # On traite la clé

        # Parcours du mot à chiffrer
        for car in motAtraiter:
            carASCII = ord(car)
            if not ((65 <= carASCII <= 90) or (97 <= carASCII <= 122)):  # Test : Si caractère n'est pas entre a-z ou A-Z

                #  On vérifie si car spécial
                if 192 <= carASCII <= 197:  # A majuscule
                    lstTemporaire.append(65)
                elif 200 <= carASCII <= 203:  # E majuscule
                    lstTemporaire.append(69)
                elif 204 <= carASCII <= 207:  # I majuscule
                    lstTemporaire.append(73)
                elif 210 <= carASCII <= 214:  # O majuscule
                    lstTemporaire.append(79)
                elif 217 <= carASCII <= 220:  # U majuscule
                    lstTemporaire.append(85)
                elif 221 == carASCII:  # Y majuscule
                    lstTemporaire.append(89)


                elif 224 <= carASCII <= 229:  # a minuscule
                    lstTemporaire.append(97)
                elif 232 <= carASCII <= 235:  # e minuscule
                    lstTemporaire.append(101)
                elif 236 <= carASCII <= 239:  # i minuscule
                    lstTemporaire.append(105)
                elif 242 <= carASCII <= 246:  # o minuscule
                    lstTemporaire.append(111)
                elif 249 <= carASCII <= 252:  # u minuscule
                    lstTemporaire.append(117)
                elif 253 == carASCII or 255 == carASCII:  # y minuscule
                    lstTemporaire.append(121)

                else:  # Caractère spécial intraitable
                    return 'Caractère spécial intraitable'

            else:
                lstTemporaire.append(carASCII)

        if inverseur:
            motChiffre = lstTemporaire.copy()
            lstTemporaire.clear()
            inverseur = False
        else:
            cleChiffre = lstTemporaire.copy()
