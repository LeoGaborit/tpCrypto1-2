"""text entrée:
IuafxvrpgpzfseRbqbokqkPrbagkeaopymVnamqswisnsTymlhesqgyvhwkpdrxsfzagkvvyn
rfahekvrltafmicyzhvujHNBqkskufrRzntdfrlavHEALPrjxvrnsmzfSgrhvunfrSVKWBTnf
fohirfXucqvupGGXEESLAecgiodyamksrChvdwmysygwttsgxsfzojgamkvronuunbuinrnff
lavcgneiisrrfbanuIzxiscuwvdsguxhytzowtisogcbizxisgnepnwefbtonktwarbqyowfz
xgsbvlvIzxisrbeiketewflrvqlhkvvtkkasvktbxhzykxctSacbmdekvryecueiuwpqlriqx
igntdttavbsayhzftnisnacimllWipqtyukMnsazyWamkJsiknZzlxibrzsgqohwheovzmsgu
qrresdampphrljtamWipqAdqjbtoavrzpwYlqxzhvywwzoSacbmdeftvzAdqjbtovydzewtjs
qXokfwgkcgnetajxKvrxejzglrjvtgzfoxesrjtfbmecwguuknqmyseuokeOBgsgnejxsmvqy
kaeNMKEWGJONZSguteumktwtjvryaeqoTdseocriaecprhoizWofzikdsglnehnseuFzxnsnq
wzxduvdhxgvpsguhukskdggxsfzwzxdmyfvbewdwxkcyovvmkmyslyevramkvrewzxdfryrGm
vdavrUEKAKMYTZBJnakfzxysyraiqqhlhnrkzzytschzYfgkmzzyjoefyxkwgOmleagxknxaj
mtnjwaksjfgzvhrretfwwjcViaeqfwnoegsrnmlzbrysZzeresjGmvdavrdrupcqobczqoerz
vdzzyloiiztkhukySQDBVJRTokrgkdcakyealyffbolEalyffjnakfzxpfrzocpaliwtntVhw
kpantwzxduvtekekaxbxvgnijaognoey

(monologue du sénateur armstrong dans metal gear rising revengeance)

taille clé : 9

//TO DO : faire en sorte qu il aille chercher le texte chiffré dans un fichier texte
"""
import math
from functools import reduce

texte_chiffré = str
texte_chiffré = "IuafxvrpgpzfseRbqbokqkPrbagkeaopymVnamqswisnsTymlhesqgyvhwkpdrxsfzagkvvynrfahekvrltafmicyzhvujHNBqkskufrRzntdfrlavHEALPrjxvrnsmzfSgrhvunfrSVKWBTnffohirfXucqvupGGXEESLAecgiodyamksrChvdwmysygwttsgxsfzojgamkvronuunbuinrnfflavcgneiisrrfbanuIzxiscuwvdsguxhytzowtisogcbizxisgnepnwefbtonktwarbqyowfzxgsbvlvIzxisrbeiketewflrvqlhkvvtkkasvktbxhzykxctSacbmdekvryecueiuwpqlriqxigntdttavbsayhzftnisnacimllWipqtyukMnsazyWamkJsiknZzlxibrzsgqohwheovzmsguqrresdampphrljtamWipqAdqjbtoavrzpwYlqxzhvywwzoSacbmdeftvzAdqjbtovydzewtjsqXokfwgkcgnetajxKvrxejzglrjvtgzfoxesrjtfbmecwguuknqmyseuokeOBgsgnejxsmvqykaeNMKEWGJONZSguteumktwtjvryaeqoTdseocriaecprhoizWofzikdsglnehnseuFzxnsnqwzxduvdhxgvpsguhukskdggxsfzwzxdmyfvbewdwxkcyovvmkmyslyevramkvrewzxdfryrGmvdavrUEKAKMYTZBJnakfzxysyraiqqhlhnrkzzytschzYfgkmzzyjoefyxkwgOmleagxknxajmtnjwaksjfgzvhrretfwwjcViaeqfwnoegsrnmlzbrysZzeresjGmvdavrdrupcqobczqoerzvdzzyloiiztkhukySQDBVJRTokrgkdcakyealyffbolEalyffjnakfzxpfrzocpaliwtntVhwkpantwzxduvtekekaxbxvgnijaognoey"
text = texte_chiffré.replace(" ", "")

def estPremier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dechiffrKasiski(texte : str) -> list:
    # Initialisation des variables
    positions = {}
    sequencesUniques = []
    toutesSequences = []
    ecartsListe = []

    for longueur in range(4, len(texte) + 1):
        for index in range(len(texte) - longueur + 1):
            sequence = texte[index:index + longueur]
            if sequence not in positions:
                positions[sequence] = []
            positions[sequence].append(index)

    for sequence, indices in positions.items():
        count = len(indices)
        if count > 1:
            toutesSequences.append((sequence, indices))

    toutesSequences.sort(key=lambda x: len(x[0]), reverse=True)

    for sequence, indices in toutesSequences:

        if not any(sequence in other for other, _ in sequencesUniques):
            sequencesUniques.append((sequence, indices))

    # Affichage des résultats
    for sequence, indices in sequencesUniques:
        gaps = [indices[i] - indices[i - 1] for i in range(1, len(indices))]


        for element in gaps:
            if estPremier(element):
                gaps.remove(element)
        if gaps != []:
            print(f"Séquence: '{sequence}' - Nombre de répétitions: {len(indices)} - Écarts: {gaps}")
            ecartsListe.append(gaps[0])
    print (ecartsListe)
    return ecartsListe

def pgcd_liste(liste):
    return reduce(math.gcd, liste)

résultat = pgcd_liste(dechiffrKasiski(text))


# Exemple d'utilisation
print(dechiffrKasiski(text))
print("taille clé :", pgcd_liste(dechiffrKasiski(text)))