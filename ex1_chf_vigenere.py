def chiffrementVigenere(motAchiffrer : str, clef : str) -> str:
    """Chiffre un mot en utilisant le chiffre de Vigenère
    Préconditions: motAchiffrer est un mot en majuscules
    Postconditions: retourne le mot chiffré"""

    for car in range(len(motAchiffrer)):

        # Variables
        codeAlphabet : int
        carASCII : int
        carCle : int
        i : int
        code : int

        facteur1 : int
        facteur2 : int

        motChiffre : [int]
        cleChiffre : [int]
        lstInt : [str]
        lstStr : [str]
        strResultat : str

        # Initialisation
        motChiffre = []
        cleChiffre = []
        lstInt = []
        lstStr = []

        # Parcours du mot à chiffrer
        for car in motAchiffrer:
            carASCII = ord(car)
            if not ((65 <= carASCII <= 90) or (97 <= carASCII <= 122)): # Test : Si caractère n'est pas entre a-z ou A-Z

                #  On vérifie si car spécial
                if 192 <= carASCII <= 197: # A majuscule
                    pass
                elif 200 <= carASCII <= 203: # E majuscule
                    pass
                elif 204 <= carASCII <= 207: # I majuscule
                    pass
                elif 210 <= carASCII <= 214: # O majuscule
                    pass
                elif 217 <= carASCII <= 220: # U majuscule
                    pass
                elif 221 == carASCII: # Y majuscule
                    pass

                elif 224 <= carASCII <= 229: # a minuscule
                    pass
                elif 232 <= carASCII <= 235: # e minuscule
                    pass
                elif 236 <= carASCII <= 239: # i minuscule
                    pass
                elif 242 <= carASCII <= 246: # o minuscule
                    pass
                elif 249 <= carASCII <= 252: # u minuscule
                    pass
                elif 253 == carASCII: # y minuscule
                    pass

                else : # Caractère spécial intraitable
                    return 'Caractère spécial intraitable'

                motChiffre.append(carASCII)
            motChiffre.append(carASCII)

        for car in clef:
            cleChiffre.append(ord(car))

        # Chiffrement
        for i in range(len(motChiffre)):  # On chiffre le mot
            carCle = cleChiffre[i % len(cleChiffre)] # Pour éviter les erreurs de dépassement

            if 65 <= motChiffre[i] <= 90: # On vérifie si la lettre du mot est en majuscule
                facteur1 = 65

            elif 97 <= motChiffre[i] <= 122: # On vérifie si la lettre du mot est en minuscule
                facteur1 = 97

            if 65 <= carCle <= 90: # On vérifie si la lettre de la clé est en majuscule
                facteur2 = 65

            elif 97 <= carCle <= 122: # On vérifie si la lettre de la clé est en minuscule
                facteur2 = 97

            code = (motChiffre[i] - facteur1 + carCle - facteur2) % 26 + facteur1

            lstInt.append(code)

        for code in lstInt:  # On convertit les chiffres en lettres
            lstStr.append(chr(code))

        strResultat = ''.join(lstStr)  # On concatène les lettres

        return motAchiffrer + " chiffré à l'aide de la clé " + clef + " donne : " + strResultat

chiffrer = "Texteclair"
clef = "Clef"
print(chiffrementVigenere(chiffrer, clef))

