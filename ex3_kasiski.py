"""text entrée:
SBGZPLPSLA OZRLLDHAZT TSKUGGURHI UEFPGZCECA WBGOZSKHDB JACOKTDZMQ
IWVANVKEHE JIQBNQRRPP WWMDPPYIFI RSDRZTKUYF WEDSHTBQHB LTLVYFTAUE
AXRAXTNEDS TQHSVSLVZT TIIIPXRQBE ETDBOACEME QBNAJGYTKM MAPLYAVJKQ
CTYEVISQIH VMHBNASSRN GBKOWNZQXM YAUCIYSBGZ PLPSLANMKE THDVMQSDIA
VBOOPLCYWP XAJGYTKMNU HTFRBWLOGY GTROXMEHPA GIVFXNXTRQ TOGERSLVMO
GYGTROXMEH ZCFWSBAEOI WGXMCGZNJN XABTYESMTM CDGASMXYTT YOGAURIHVP
DAZFWRFUJP SMRHZNHARU ZEKHHJXUII JHEWSNTSRN GKUXDSJUVK UYEUKEUAGF
QLVTFPRQNP RRNQTIDRCD ZIXUXTFTKM SMIHVMDBOO PLCYDLBMCC VDFWSBJTVR
LHKPHCYEPM YAUTYESZKE TNKMHBNASS WOUJXQPKZN JUUPTRECUG VFDSPSWMSE
DFKEQQTHDL MEVWRHXNXC DZKRJLCYFW TEIRLCWMJB GOSLHUYUCP LRHUGFWEDA
WQIEIHVBHA ZWCONNEMOZ VIETHOKDUA TTRZOLPTZO QXNRDGQZUDN KOPIZTTMRT
LKGXPNRLBA OEDFTRBXZA VRRPKQIMAG FRLBNYHCIY

taille clé : 8
"""
import math
from functools import reduce
import os



texte_chiffré = str
texte_chiffré = "SBGZPLPSLA OZRLLDHAZT TSKUGGURHI UEFPGZCECA WBGOZSKHDB JACOKTDZMQ IWVANVKEHE JIQBNQRRPP WWMDPPYIFI RSDRZTKUYF WEDSHTBQHB LTLVYFTAUE AXRAXTNEDS TQHSVSLVZT TIIIPXRQBE ETDBOACEME QBNAJGYTKM MAPLYAVJKQ CTYEVISQIH VMHBNASSRN GBKOWNZQXM YAUCIYSBGZ PLPSLANMKE THDVMQSDIA VBOOPLCYWP XAJGYTKMNU HTFRBWLOGY GTROXMEHPA GIVFXNXTRQ TOGERSLVMO GYGTROXMEH ZCFWSBAEOI WGXMCGZNJN XABTYESMTM CDGASMXYTT YOGAURIHVP DAZFWRFUJP SMRHZNHARU ZEKHHJXUII JHEWSNTSRN GKUXDSJUVK UYEUKEUAGF QLVTFPRQNP RRNQTIDRCD ZIXUXTFTKM SMIHVMDBOO PLCYDLBMCC VDFWSBJTVR LHKPHCYEPM YAUTYESZKE TNKMHBNASS WOUJXQPKZN JUUPTRECUG VFDSPSWMSE DFKEQQTHDL MEVWRHXNXC DZKRJLCYFW TEIRLCWMJB GOSLHUYUCP LRHUGFWEDA WQIEIHVBHA ZWCONNEMOZ VIETHOKDUA TTRZOLPTZO QXNRDGQZUDN KOPIZTTMRT LKGXPNRLBA OEDFTRBXZA VRRPKQIMAG FRLBNYHCIY"

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



# Exemple d'utilisation
print(dechiffrKasiski(text))
print("taille clé :", pgcd_liste(dechiffrKasiski(text)))