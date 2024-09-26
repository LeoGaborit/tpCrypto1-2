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

        motChiffre : [int]
        cleChiffre : [int]
        lstInt : [str]
        lstStr : [str]
        strResultat : str

        # Initialisation
        codeAlphabet = 0
        carASCII = 0
        carCle = 0
        i = 0
        code = 0

        motChiffre = []
        cleChiffre = []
        lstInt = []
        lstStr = []
        strResultat = ""

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

            if carASCII % 2 != 0: # Si impair
                motChiffre.append(carASCII-1)
            else : # Si pair
                motChiffre.append(carASCII)

        for car in clef:
            if ord(car) % 2 != 0: # Si impair
                cleChiffre.append(ord(car)-1)
            else : # Si pair
                cleChiffre.append(ord(car))


        # Chiffrement
        for i in range(len(motChiffre)):  # On chiffre le mot
            carCle = cleChiffre[i % len(cleChiffre)]

            if 65 <= motChiffre[i] <= 90:  # Majuscule
                codeAlphabet = (motChiffre[i] - 64 + carCle - 64) % 26 + 64 # +64 pour revenir à la table ASCII (majuscule)

            elif 97 <= motChiffre[i] <= 122:  # Minuscule
                codeAlphabet = (motChiffre[i] - 96 + carCle - 96) % 26 + 96 # +96 pour revenir à la table ASCII (minuscule)

            lstInt.append(codeAlphabet)

        for code in lstInt:  # On convertit les chiffres en lettres
            lstStr.append(chr(code))

        strResultat = ''.join(lstStr)  # On concatène les lettres

        return motAchiffrer + " chiffré à l'aide de la clé " + clef + " donne : " + strResultat

chiffrer = "Texteclair"
clef = "Clef"
print(chiffrementVigenere(chiffrer, clef))

