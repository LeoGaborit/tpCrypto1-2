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

def racisme_absolu(texteEntree : list) :

    # Initialisation
    i : int
    j : int
    k : int
    m : int
    n : int
    doublon : int

    cleTri : str
    cleActuelle : str
    cleSupposee : str

    clesGardees = [str]

    # Valeurs
    i, j, m, n = 0, 0, 0, 0
    doublon = 0
    k = 3
    cleActuelle = ""
    cleSupposee = ""
    clesGardees = []

    for k in range(3, (len(texteEntree)//2) - 1) :          # On définit la taille de la clé, puis l'agrandit au cours du temps
        for i in range(0, (len(texteEntree)-k+1)):
            doublon = 0
            cleActuelle = ""
            for m in range(k) :
                cleActuelle += texteEntree[i+m]

            for j in range(i, len(texteEntree)-k+1) :
                cleSupposee = ""
                for n in range(k):
                    cleSupposee += texteEntree[j+n]

                if doublon == 0:
                    doublon = 1
                else:
                    if cleActuelle == cleSupposee:
                        print("Répétition trouvée : ", cleActuelle, " Indice : ", j)
                        clesGardees.append(cleActuelle)
                        doublon = 0

    # Tri des occurences
    for cleTri in clesGardees :
        if cleTri in clesGardees[-1] :
            clesGardees.remove(cleTri)

    print(clesGardees)


import math


def kasiski_analysis(texteEntree: list):
    # Initialisation
    clesGardees = []

    # Parcourir différentes tailles de clés possibles (à partir de 3 jusqu'à la moitié du texte)
    for k in range(3, len(texteEntree) // 2):
        # Parcourir le texte pour chercher les répétitions de taille k
        for i in range(0, len(texteEntree) - k):
            cleActuelle = ''.join(texteEntree[i:i + k])

            # Chercher la clé actuelle dans le reste du texte
            for j in range(i + 1, len(texteEntree) - k):
                cleSupposee = ''.join(texteEntree[j:j + k])

                # Si une répétition est trouvée, on la garde
                if cleActuelle == cleSupposee:
                    print(f"Répétition trouvée : {cleActuelle} Indice : {i} et {j}")
                    clesGardees.append((cleActuelle, i, j))

    # Suppression des sous-chaînes
    clesUniques = list(set([cle for cle, _, _ in clesGardees]))

    # Filtrer les clés qui sont des sous-chaînes d'autres clés plus longues
    clesFiltrees = []
    distances = []
    for cle, i, j in clesGardees:
        if not any(cle != autreCle and cle in autreCle for autreCle in clesUniques):
            clesFiltrees.append(cle)
            distances.append(j - i)  # Calcul de la distance entre les répétitions

    print("Clés retenues après filtrage :")
    print(clesFiltrees)

    # Calculer le PGCD des distances
    if len(distances) > 1:
        pgcd = distances[0]
        for d in distances[1:]:
            pgcd = math.gcd(pgcd, d)
        print(f"Le PGCD des distances est : {pgcd}")
    else:
        print("Pas assez de répétitions pour calculer le PGCD.")

    return clesFiltrees


# Exemple d'utilisation
kasiski = list("DLOMGKVVWQCUAPREOQJSTLMXQCUAPRVLFXRESIME")
kasiski_analysis(kasiski)

#racisme_absolu(kasiski)

