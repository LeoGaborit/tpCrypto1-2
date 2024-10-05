import math
from functools import reduce

texte_chiffré = "IuafxvrpgpzfseRbqbokqkPrbagkeaopymVnamqswisnsTymlhesqgyvhwkpdrxsfzagkvvynrfahekvrltafmicyzhvujHNBqkskufrRzntdfrlavHEALPrjxvrnsmzfSgrhvunfrSVKWBTnffohirfXucqvupGGXEESLAecgiodyamksrChvdwmysygwttsgxsfzojgamkvronuunbuinrnfflavcgneiisrrfbanuIzxiscuwvdsguxhytzowtisogcbizxisgnepnwefbtonktwarbqyowfzxgsbvlvIzxisrbeiketewflrvqlhkvvtkkasvktbxhzykxctSacbmdekvryecueiuwpqlriqxigntdttavbsayhzftnisnacimllWipqtyukMnsazyWamkJsiknZzlxibrzsgqohwheovzmsguqrresdampphrljtamWipqAdqjbtoavrzpwYlqxzhvywwzoSacbmdeftvzAdqjbtovydzewtjsqXokfwgkcgnetajxKvrxejzglrjvtgzfoxesrjtfbmecwguuknqmyseuokeOBgsgnejxsmvqykaeNMKEWGJONZSguteumktwtjvryaeqoTdseocriaecprhoizWofzikdsglnehnseuFzxnsnqwzxduvdhxgvpsguhukskdggxsfzwzxdmyfvbewdwxkcyovvmkmyslyevramkvrewzxdfryrGmvdavrUEKAKMYTZBJnakfzxysyraiqqhlhnrkzzytschzYfgkmzzyjoefyxkwgOmleagxknxajmtnjwaksjfgzvhrretfwwjcViaeqfwnoegsrnmlzbrysZzeresjGmvdavrdrupcqobczqoerzvdzzyloiiztkhukySQDBVJRTokrgkdcakyealyffbolEalyffjnakfzxpfrzocpaliwtntVhwkpantwzxduvtekekaxbxvgnijaognoey"
text = texte_chiffré.replace(" ", "")

def estPremier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dechiffrKasiski(texte: str) -> list:
    # Initialisation des variables
    positions = {}
    sequencesUniques = []
    toutesSequences = []
    ecartsListe = []

    # Parcourir les séquences répétées de longueur >= 4
    for longueur in range(4, len(texte) + 1):
        for index in range(len(texte) - longueur + 1):
            sequence = texte[index:index + longueur]
            if sequence not in positions:
                positions[sequence] = []
            positions[sequence].append(index)

    # Identifier les séquences répétées
    for sequence, indices in positions.items():
        count = len(indices)
        if count > 1:
            toutesSequences.append((sequence, indices))

    toutesSequences.sort(key=lambda x: len(x[0]), reverse=True)

    for sequence, indices in toutesSequences:
        if not any(sequence in other for other, _ in sequencesUniques):
            sequencesUniques.append((sequence, indices))

    # Calculer les écarts entre les répétitions
    for sequence, indices in sequencesUniques:
        gaps = [indices[i] - indices[i - 1] for i in range(1, len(indices))]

        # Filtrer les écarts qui ne sont pas premiers
        gaps = [gap for gap in gaps if not estPremier(gap)]

        # Si on a des écarts restants, les afficher et les stocker
        if gaps:
            #print(f"Séquence: '{sequence}' - Nombre de répétitions: {len(indices)} - Écarts: {gaps}")
            ecartsListe.append(gaps[0])

    return ecartsListe

def pgcd_liste(liste):
    if len(liste) == 0:
        return None
    return reduce(math.gcd, liste)

def dechiffrKasiskiTest(listeEssai: list):
    print("Tests Kasiski : ")
    for chaine in listeEssai:
        ecarts = dechiffrKasiski(chaine)
        if ecarts:
            print(f"Pour {chaine} : Taille de clé probable = {pgcd_liste(ecarts)}")
        else:
            print(f"Pour {chaine} : Impossible de déterminer la taille de clé (pas assez de répétitions).")

essaisJeux = [
    "ABCDABCDABCDABCD",  # Taille de clé : 4
    "XYZXYZXYZXYZXYZXYZ",  # Taille de clé : 3
    "HELLOWORLDHELLOWORLDHELLOWORLD",  # Taille de clé : 10
    "QWERTYQWERTYQWERTYQWERTY",  # Taille de clé : 6
    "MNBVCXASDFGHMNBVCXASDFGHMNBVCXASDFGH"  # Taille de clé : 12
]

dechiffrKasiskiTest(essaisJeux)
