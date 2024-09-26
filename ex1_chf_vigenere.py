def chiffrementVigenere(motAchiffrer : str, clef : str) -> str:
    """Chiffre un mot en utilisant le chiffre de Vigenère
    Préconditions: motAchiffrer est un mot en majuscules
    Postconditions: retourne le mot chiffré"""

    for car in range(len(motAchiffrer)):
        carAlphab : str
        carASCII : int

        motChiffre : [int]
        cleChiffre : [int]
        lstResultat : [str]
        strResultat : str

        carAlphabet = ""
        carASCII = 0
        motChiffre = []
        cleChiffre = []
        lstResultat = []
        strResultat = ""

        # Parcours du mot à chiffrer
        for car in range(len(motAchiffrer)):
            carASCII = ord(motAchiffrer[car])
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

            else:
                motChiffre.append(carASCII)

            for carASCII in range(len(clef)):
                cleChiffre.append(ord(clef[carASCII]))

            # Chiffrement
            for car in range(len(motChiffre)):
                lstResultat.append(chr(motChiffre[car] + cleChiffre[car % len(cleChiffre)]))
    print(lstResultat)

    return motChiffre

chiffrer = "Bonjour"
clef = "Clef"
chiffrementVigenere(chiffrer, clef)
