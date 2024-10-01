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

texte_chiffré = str
texte_chiffré = "SBGZPLPSLA OZRLLDHAZT TSKUGGURHI UEFPGZCECA WBGOZSKHDB JACOKTDZMQ IWVANVKEHE JIQBNQRRPP WWMDPPYIFI RSDRZTKUYF WEDSHTBQHB LTLVYFTAUE AXRAXTNEDS TQHSVSLVZT TIIIPXRQBE ETDBOACEME QBNAJGYTKM MAPLYAVJKQ CTYEVISQIH VMHBNASSRN GBKOWNZQXM YAUCIYSBGZ PLPSLANMKE THDVMQSDIA VBOOPLCYWP XAJGYTKMNU HTFRBWLOGY GTROXMEHPA GIVFXNXTRQ TOGERSLVMO GYGTROXMEH ZCFWSBAEOI WGXMCGZNJN XABTYESMTM CDGASMXYTT YOGAURIHVP DAZFWRFUJP SMRHZNHARU ZEKHHJXUII JHEWSNTSRN GKUXDSJUVK UYEUKEUAGF QLVTFPRQNP RRNQTIDRCD ZIXUXTFTKM SMIHVMDBOO PLCYDLBMCC VDFWSBJTVR LHKPHCYEPM YAUTYESZKE TNKMHBNASS WOUJXQPKZN JUUPTRECUG VFDSPSWMSE DFKEQQTHDL MEVWRHXNXC DZKRJLCYFW TEIRLCWMJB GOSLHUYUCP LRHUGFWEDA WQIEIHVBHA ZWCONNEMOZ VIETHOKDUA TTRZOLPTZO QXNRDGQZUDN KOPIZTTMRT LKGXPNRLBA OEDFTRBXZA VRRPKQIMAG FRLBNYHCIY"

text = texte_chiffré.replace(" ", "")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_repetitions_and_gaps(text):
    positions = {}

    # Parcours du texte pour enregistrer les positions de chaque séquence de longueur 2 ou plus
    for sequence_length in range(3, len(text) + 1):  # Séquences de longueur 2 à la longueur totale du texte
        for index in range(len(text) - sequence_length + 1):
            sequence = text[index:index + sequence_length]
            if sequence not in positions:
                positions[sequence] = []
            positions[sequence].append(index)

    # Liste pour stocker toutes les séquences avec leurs indices
    all_sequences = []

    # Ajout des séquences avec leurs positions à la liste
    for sequence, indices in positions.items():
        count = len(indices)
        if count > 1:
            all_sequences.append((sequence, indices))

    # Tri des séquences par longueur décroissante
    all_sequences.sort(key=lambda x: len(x[0]), reverse=True)

    # Liste pour stocker les séquences uniques
    unique_sequences = []

    # Filtrage des séquences uniques
    for sequence, indices in all_sequences:
        # Vérifier si la séquence n'est pas incluse dans une séquence plus longue
        if not any(sequence in other for other, _ in unique_sequences):
            unique_sequences.append((sequence, indices))

    # Affichage des résultats
    for sequence, indices in unique_sequences:
        gaps = [indices[i] - indices[i - 1] for i in range(1, len(indices))]
        for element in gaps:
            if is_prime(element):
                gaps.remove(element)
        if gaps != []:
            print(f"Séquence: '{sequence}' - Nombre de répétitions: {len(indices)} - Écarts: {gaps}")

# Exemple d'utilisation
texte = "abracadabra"
count_repetitions_and_gaps(text)
